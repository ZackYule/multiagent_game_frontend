import random
import streamlit as st
from PIL import Image
from dataclasses import dataclass
from typing import Optional


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
user1 = User(name="Regina", avatar="avatars/截屏2024-12-22 01.19.26.png")
user2 = User(name="Guohao", avatar="avatars/截屏2024-12-22 01.19.53.png")
user3 = User(name="CoCo", avatar="avatars/截屏2024-12-22 01.20.02.png")
user4 = User(name="Wendong", avatar="avatars/截屏2024-12-22 01.20.10.png")
user5 = User(name="Zack", avatar="avatars/截屏2024-12-22 01.20.19.png")
user6 = User(name="Tianqi", avatar="avatars/截屏2024-12-22 01.20.24.png")
user7 = User(name="Ziyi", avatar="avatars/image.png")

users = [user1, user2, user3, user4, user5, user6, user7]

# 使用 Streamlit session_state 来存储消息列表，避免刷新时丢失数据
if "messages" not in st.session_state:
    st.session_state.messages = []

# 设置页面标题
st.set_page_config(page_title="发帖界面", layout="wide")
st.title("multi agent角色扮演")

# 创建左右两栏
col1, col2 = st.columns([2, 1])  # 设置比例，2:1

# 在第二列（col2）添加内容，用户输入新的帖子
with col2:
    with st.container():
        st.header("任务栏")
        # task_content = st.text_input("请输入你的任务:")
        st.write("task_content")

    with st.container():
        st.header("发布帖子")
        input_content = st.text_input("请输入你的帖子:")

        # 发布按钮
        if st.button("发布"):
            if input_content.strip():  # 确保内容不为空
                # 创建新的消息对象
                new_message = Message(
                    user=random.choice(users), content=input_content.strip()
                )
                # 将新消息添加到消息列表
                st.session_state.messages.append(new_message)
                st.success("帖子发布成功！")

                # 强制重新渲染界面，避免上一条消息留存
                # st.experimental_rerun()  # 强制刷新，重新渲染界面
            else:
                st.error("帖子内容不能为空！")

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
                st.write("💬 35")
            with small_col2:
                st.write("🔁 326")
            with small_col3:
                st.write("❤️ 2,280")
            with small_col4:
                st.write("👁️ 34万")
