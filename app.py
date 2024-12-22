import random
import sys
import streamlit as st
from PIL import Image
from dataclasses import dataclass
from typing import Optional
from scripts.reddit_game_demo.game import main


if "task_queue" not in st.session_state:
    st.session_state.task_queue = []


# 定义用户类
@dataclass
class User:
    name: str  # 用户的名字
    avatar: Optional[str] = None  # 用户的头像，默认为 None，头像可以是图片路径或 URL


# 定义消息类
@dataclass
class Message:
    user: User  # 消息发送者，类型为 User
    content: str  # 消息内容


# 初始化用户
user1 = User(name="Regina(Player)", avatar="avatars/截屏2024-12-22 01.19.26.png")
user2 = User(name="Shiguan(Agent)", avatar="avatars/截屏2024-12-22 01.19.53.png")
user3 = User(name="CoCo(Agent)", avatar="avatars/截屏2024-12-22 01.20.02.png")
user4 = User(name="Panguan(Agent)", avatar="avatars/截屏2024-12-22 01.20.10.png")
user5 = User(name="Lingpo(Agent)", avatar="avatars/截屏2024-12-22 01.20.19.png")
user6 = User(name="Weizhi(Agent)", avatar="avatars/截屏2024-12-22 01.20.24.png")
user7 = User(name="Jiaoshou(Agent)", avatar="avatars/image.png")

users = [user1, user3, user4, user5, user6, user7]

# 使用 Streamlit session_state 来存储消息列表，避免刷新时丢失数据
if "messages" not in st.session_state:
    st.session_state.messages = []

# 设置页面标题
st.set_page_config(page_title="发帖界面", layout="wide")
st.title("multi agent角色扮演")

# 创建一个空容器，用于动态更新消息
message_container = st.empty()

# 创建左右两栏
col1, col2 = st.columns([2, 1])  # 设置比例，2:1

# 在第二列（col2）添加内容，用户输入新的帖子
with col2:
    with st.container():
        st.header("发布帖子")
        input_content = st.text_input("请输入你的帖子:")

        # 发布按钮
        if st.button("发布"):
            if input_content.strip():  # 确保内容不为空
                st.session_state.task_queue.append(input_content.strip())
                new_message = Message(user=users[0], content=input_content.strip())
                st.session_state.messages.append(new_message)
                st.success("帖子发布成功！")
            else:
                st.error("帖子内容不能为空！")

    with st.container():
        st.header("任务栏")
        # task_content = st.text_input("请输入你的任务:")
        st.markdown(
            "<h3 style='color: #FF6347;'>请识别这些玩家的职业 😎</h3>",
            unsafe_allow_html=True,
        )

        users2 = [user2, user3, user4, user5, user6, user7]

        # 显示用户头像和名字，猜测职业
        for user in users2:
            st.image(user.avatar, width=50)
            st.text(user.name)

            # 输入框，让用户猜职业
            job = st.text_input(f"你觉得 {user.name} 的职业是什么?", key=user.name)

            # 在用户提交输入后显示结果
            if job:
                st.write(f"你猜测 {user.name} 的职业是: {job}")

# 在第一列（col1）显示消息列表
with col1:
    with st.container():
        st.header("聊天栏")
        st.text("这是左栏的内容，可以放置文本、图片、按钮等元素。")

        # 按逆序显示所有的消息
        for idx, message in enumerate(reversed(st.session_state.messages)):
            avatar_col1, avatar_col2 = st.columns([1, 9])

            with avatar_col1:
                # 上传头像
                if message.user.avatar:
                    avatar = Image.open(message.user.avatar)  # 替换为你的头像图片路径
                    st.image(avatar, width=50)  # 设置头像宽度

            with avatar_col2:
                # 显示用户名字
                st.markdown(f"### {message.user.name}", unsafe_allow_html=True)

            # 显示消息内容
            st.markdown(
                "<span style='color: gray;'>@dr_cintas · 12月20日</span>",
                unsafe_allow_html=True,
            )
            st.markdown(message.content)

            # 底部图标部分
            small_col1, small_col2, small_col3, small_col4 = st.columns(4)
            with small_col1:
                st.write(f"💬 {random.randint(10, 100)}")
            with small_col2:
                st.write(f"🔁 {random.randint(100, 1000)}")
            with small_col3:
                st.write(f"❤️ {random.randint(1000, 5000)}")
            with small_col4:
                st.write(f"👁️ {random.randint(100000, 500000)}")


# 模拟命令行参数
sys.argv = [
    "scripts/reddit_game_demo/game.py",  # 这里是脚本名称，一般可为任意值
    "--config_path",
    "scripts/reddit_game_demo/game.yaml",  # 传递的参数
]
main()
