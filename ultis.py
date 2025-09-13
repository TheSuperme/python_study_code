"""
    尝试将字节数组解码为字符串。

    该函数首先尝试使用 'UTF-8' 编码解码字节数组。
    如果 'UTF-8' 解码失败（例如，因为字节数组不是有效的 UTF-8 编码），
    它会回退到使用 'GBK' 编码进行解码。

    Args:
        bytes_arr (bytes): 需要解码的字节数组。

    Returns:
        str: 解码后的字符串。
"""
def decode_data(bytes_arr:bytes):
    try:
        msg = bytes_arr.decode('UTF-8')
    except:
        msg = bytes_arr.decode('GBK')

    return msg