import streamlit as st
import auth


def _set_authenticated(email):
    """Set authenticated state in session."""
    st.session_state["authenticated"] = True
    st.session_state["user_email"] = email
    st.rerun()


def _handle_sign_in(email, password, sidebar):
    """Handle sign in logic."""
    if auth.login(email, password):
        _set_authenticated(email)
    else:
        sidebar.error("Invalid email or password.")


def _handle_sign_up(username, email, password, sidebar):
    """Handle sign up logic."""
    if not username:
        sidebar.error("Username is required.")
        return
    ok, msg = auth.register(username, email, password)
    if ok:
        _set_authenticated(email)
    else:
        sidebar.error(msg or "Registration failed.")


def _display_authenticated(sidebar):
    """Display authenticated user info and sign out button."""
    sidebar.success(f"Signed in as\n{st.session_state['user_email']}")
    if sidebar.button("Sign Out", use_container_width=True):
        st.session_state["authenticated"] = False
        st.session_state["user_email"] = None
        st.rerun()


def sidebar_display():
    sidebar = st.sidebar
    sidebar.title("🔐 Account")

    if st.session_state.get("authenticated"):
        _display_authenticated(sidebar)
        return

    mode = sidebar.radio("", ["Sign In", "Sign Up"], horizontal=True)

    with sidebar.form("auth_form"):
        username = st.text_input("Username") if mode == "Sign Up" else None
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button(mode, use_container_width=True)

    if submitted:
        if not email or not password:
            sidebar.error("Email and password are required.")
            return

        if mode == "Sign In":
            _handle_sign_in(email, password, sidebar)
        else:
            _handle_sign_up(username, email, password, sidebar)
