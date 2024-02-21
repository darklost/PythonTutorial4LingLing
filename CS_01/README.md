# `PDF`文档转换`WORD`文档

## 版本信息

| 时间       | 信息 | 作者 |
| ---------- | ---- | ---- |
| 2023-12-05 | 新建 | D.K. |

## 安装依赖

```shell
pip install pdf2docx
```

## 原理

使用`pdf2docx`库中的`Converter`类调用`convert`方法将`pdf`文件转换为`word`文件

## 使用

```shell

python main.py --pdf_file ./test.pdf --docx_file ./test.docx

```
