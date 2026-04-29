import streamlit as st
import auth


def sidebar_display():
    sidebar = st.sidebar
    sidebar.title("🔐 Account")

    if st.session_state.get("authenticated"):
        sidebar.success(f"Signed in as\n{st.session_state['user_email']}")
        if sidebar.button("Sign Out", use_container_width=True):
            st.session_state["authenticated"] = False
            st.session_state["user_email"] = None
            st.rerun()
        return

    mode = sidebar.radio("", ["Sign In", "Sign Up"], horizontal=True)

    with sidebar.form("auth_form"):
        if mode == "Sign Up":
            username = st.text_input("Username")
        else:
            username = None
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button(mode, use_container_width=True)

    if submitted:
        if not email or not password:
            sidebar.error("Email and password are required.")
            return

        if mode == "Sign In":
            if auth.login(email, password):
                st.session_state["authenticated"] = True
                st.session_state["user_email"] = email
                st.rerun()
            else:
                sidebar.error("Invalid email or password.")
        else:
            if not username:
                sidebar.error("Username is required.")
                return
            ok, msg = auth.register(username, email, password)
            if ok:
                st.session_state["authenticated"] = True
                st.session_state["user_email"] = email
                st.rerun()
            else:
                sidebar.error(msg or "Registration failed.")
