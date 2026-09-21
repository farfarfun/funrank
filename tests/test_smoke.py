"""funrank 占位包的最小可发布性测试。"""

import funrank


def test_placeholder_public_surface() -> None:
    """占位包应保持明确的版本字符串，不虚构尚未实现的 API。"""
    assert funrank.__version__ == "0.0.1"
