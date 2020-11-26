# 串口工具使用手册

参考 [pySerial 3.4](https://pyserial.readthedocs.io/en/latest/)。

`pySerial` 模块封装了对串行端口（serial port）的访问。它提供了在 Windows，OSX，Linux，BSD（可能是任何 POSIX 兼容系统）和 IronPython 上运行的 Python 的后端。模块名为“`serial`”会自动选择适当的后端。

<details>
<summary>pySerial 主要的特点</summary>

- 在所有支持的平台上基于相同类的接口。
- 通过 Python 属性访问端口设置。
- 通过 RTS/CTS 和/或 Xon/Xoff 支持不同的字节大小，停止位，奇偶校验和流程控制。
- 有或没有超时的功能设定。
- 像 API 这样的文件，带有“`read`”和“`write`”（也支持“`readline`”等）。
- 该软件包中的文件是 100% 纯 Python。
- 该端口已设置为二进制传输。没有 NULL 字节剥离，CR-LF 转换等（对于 POSIX 启用了很多次）。这使该模块具有通用性。
- 与 `io` 库兼容
- 示例中提供的 RFC 2217 客户端（实验）服务器。

</details>
