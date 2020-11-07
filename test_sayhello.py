import unittest
from app import app, db
from app.models import Message
from app.fakes import forge

class SayHelloTestCase(unittest.TestCase):
    def setUp(self):
        # 设置配置
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )

        db.create_all()
        message = Message(name='test1', body='test1 message')
        db.session.add(message)
        db.session.commit()

        # 创建测试客户端
        self.client = app.test_client()
        # 创建测试命令行运行器
        self.runner = app.test_cli_runner()

    def tearDown(self):
        # 拆卸配置
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        # 测试程序实例是否存在
        self.assertIsNotNone(app)

    def test_app_is_testing(self):
        # 测试程序是否处在测试模式
        self.assertTrue(app.config['TESTING'])

    def test_404_page(self):
        # 测试 404 页面
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertIn('Page Not Found - 404', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 404)

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('1 messages', data)
        self.assertIn('test1 message', data)
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/', data=dict(
            name='New Name',
            message='New Message',
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('New Name', data)
        self.assertIn('New Message', data)

    def test_forge_command(self):
        # 测试虚拟数据
        result = self.runner.invoke(forge)
        self.assertIn('Generating 100 messages...', result.output)
        self.assertEqual(Message.query.count(), 100)


if __name__ == '__main__':
    unittest.main()
