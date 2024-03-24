import sys
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.edge.service import Service

def get_foreign_exchange_rate(date, currency_code):
    # 设置 Edge WebDriver 的选项
    edge_options = EdgeOptions()
    edge_options.use_chromium = True  # 使用 Chromium 内核
    edge_options.add_argument('--headless')  # 无头模式，不打开浏览器窗口
    
    # 指定 Edge WebDriver 的可执行文件路径
    edge_driver_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'

    # 创建 Edge WebDriver
    # 通过service方法打开路径
    service = Service(edge_driver_path)
    # 再去调用
    driver = webdriver.Edge(service=service)
    
    # 打开中国银行外汇牌价网站
    url = 'https://www.boc.cn/sourcedb/whpj/'
    driver.get(url)
    
    try:
        # 输入日期
        date_input = driver.find_element_by_css_selector('input[name="erectDate"]')
        date_input.clear()
        date_input.send_keys(date)
        print("Date input:", date)
        
        # 选择货币
        currency_select = driver.find_element_by_css_selector('select[name="pjname"]')
        currency_select.find_element_by_xpath(f'//option[text()="{currency_code}"]').click()
        print("Currency selected:", currency_code)
        
        # 点击查询按钮
        query_button = driver.find_element_by_css_selector('input[type="button"][value="查询"]')
        query_button.click()
        print("Query button clicked")
        
        # 获取现汇卖出价
        exchange_rate = driver.find_element_by_css_selector('td:nth-child(5)').text
        print("Exchange rate:", exchange_rate)
        
        return exchange_rate
    except NoSuchElementException:
        return None
    finally:
        driver.quit()

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
        sys.exit(1)
    
    date = sys.argv[1]
    currency_code = sys.argv[2]
    
    try:
        exchange_rate = get_foreign_exchange_rate(date, currency_code)
        if exchange_rate is not None:
            with open("result.txt", "w") as file:
                file.write(f"The exchange rate of {currency_code} on {date} is: {exchange_rate}")
            print(f"The exchange rate of {currency_code} on {date} is: {exchange_rate}")
        else:
            print("No data available")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()