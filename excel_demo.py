# -*- coding: utf-8 -*-
# @Date : 2017-01-17
# @Function : Excel操作样例
# @Author : liujianzhu

import os
import xlrd
import xlwt

FPDM_COL_INDEX = 25
FPHM_COL_INDEX = 26
ORDER_COL_INDEX = 42
GOODSID_COL_INDEX = 38

# C:\Users\liujianzhu\Desktop\test.xls

def get_data():
    """获取Excel数据源"""
    filepath = raw_input(u'请将xls文件路径粘贴进去，按Enter键继续：')
    is_valid = False  # 验证文件
    try:
        print filepath
        # 判断给出的路径是不是xls格式
        if os.path.isfile(filepath):
            filename = os.path.basename(filepath)
            if filename.split('.')[1] == 'xls':
                is_valid = True
        data = None
        if is_valid:
            data = xlrd.open_workbook(filepath)
    except Exception, e:
        print u'你操作错误：%s' % e
        return None
    return data


def handle_data():
    """处理数据"""
    data = get_data()
    if data:
        try:
            table = data.sheet_by_index(0)
            nrows = table.nrows

            print(u'正在检索中...')
            for i in xrange(nrows):
                write_data(table.row_values(i))
                if i == 0:
                    print(u'第一行是表头，不处理...')
                    continue
                fpdm = table.cell(i, FPDM_COL_INDEX).value
                fphm = table.cell(i, FPHM_COL_INDEX).value
                goods_id = table.cell(i, GOODSID_COL_INDEX).value
                order_id = table.cell(i, ORDER_COL_INDEX).value
                print(u'%s: 发货单号: %s , 商品编码: %s , 发票轨号: %s , 发票号码: %s' % (i, goods_id, order_id, fpdm, fphm))
        except Exception, e:
            print(u'操作错误：%s' % e)
            return None
    else:
        print(u'操作失败')
        return None

def write_data(data):
    """写excel数据"""
    file = xlwt.Workbook()
    table = file.add_sheet("sheet-2", cell_overwrite_ok=True)
    l = 0 # 行
    for line in data:
        c = 0
        for col in line:
            table.write(l, c, line[c])
            c += 1
        l += 1
    file_path = r'C:\Users\liujianzhu\Desktop\out.xls'
    file.save(file_path)

def main():
    handle_data()

if __name__ == '__main__':
    main()