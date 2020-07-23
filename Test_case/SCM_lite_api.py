import requests
import unittest
from SCM_Lite import HTMLTestRunner
# from ddt import ddt, data, unpack
import random

host = "http://114.119.183.204"
port = "3150"
headers = {'Content-Type': 'application/json',
           'Authorization': 'eyJhbGciOiJIUzI1NiJ9.'
                            'eyJpZCI6MjQsImNvbXBhb'
                            'nlfaWQiOjEsIndhcnNob3V'
                            'zZV9pZCI6MSwicm9sZV9pZ'
                            'CI6MSwidXNlcm5hbWUiOiJ'
                            'hZG1pbiIsImNyZWF0ZWRfd'
                            'GltZSI6IjIwMjAtMDMtMjY'
                            'gMTI6MTc6MjUiLCJjcmVhd'
                            'GVkX2J5IjoxLCJzdGF0ZSI'
                            '6IjEiLCJ1cGRhdGVkX3Rpb'
                            'WUiOiIyMDIwLTAzLTMwIDE'
                            '0OjM2OjA3IiwidXBkYXRlZ'
                            'F9ieSI6MSwiZGVsZXRlZCI'
                            '6MCwiZGlzYWJsZWQiOjB9.'
                            'Zca4D6vlOWhsBxEjas296J'
                            'hN-46mm6ICDnMkdNeUdXk'}


# @ddt
class SCMScenarioOneTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.g = globals()

    @classmethod
    def tearDownClass(self):
        pass

    def Test_01_SignIn(self):
        url = host + ":" + port + "/login"

        body = {
            "username": "admin",
            "password": "admin123"
        }

        r = requests.post(url=url, json=body, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_02_NewUom(self):
        url = host + ":" + port + "/uom/create"
        uom_name = "Package" + str(random.randint(10, 9999))

        body = {
            "name": uom_name
        }

        r = requests.post(url=url, json=body, headers=headers)

        new_uom_id = r.json()["data"]["id"]
        # Assert
        self.g['UOMId'] = new_uom_id
        self.g['UOMName'] = uom_name
        self.assertEqual(200, r.status_code, "Code should be 200!")
        # return self.g['UOMId'], self.g['UOMName']

    def test_03_SearchUom(self):
        url = host + ":" + port + "/uom/detail"

        params = {"id": self.g['UOMId']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_04_NewCategory(self):
        url = host + ":" + port + "/category/create"
        category_name = "Food" + str(random.randint(10, 9999))

        body = {
            "sku_id": 1,
            "category_type": "Company_category",
            "name": category_name
        }

        r = requests.post(url=url, json=body, headers=headers)

        new_category_id = r.json()["data"]["insertId"]
        # print(r.json()["data"]["insertId"])
        # Assert
        self.g['CategoryId'] = new_category_id
        self.assertEqual(200, r.status_code, "Code should be 200!")
        return self.g['CategoryId']

    def test_05_NewSubCategory(self):
        url = host + ":" + port + "/category/sub/create"
        sub_category_name = "SubFood" + str(random.randint(10, 9999))

        body = {
            "sku_category_id": self.g['CategoryId'],
            "name": sub_category_name
        }

        r = requests.post(url=url, json=body, headers=headers)

        new_sub_category_id = r.json()["data"]["insertId"]

        # Assert
        self.g['SubCategoryId'] = new_sub_category_id
        self.assertEqual(200, r.status_code, "Code should be 200!")
        return self.g['SubCategoryId']

    def test_06_SearchCategoryInPages(self):
        url = host + ":" + port + "/category/page"

        body = {
            "draw": 1,
            "columns": [
                {
                    "data": "updated_time",
                    "name": "",
                    "searchable": "true",
                    "orderable": "true",
                    "search": {
                        "value": "",
                        "regex": "false"
                    }
                }
            ],
            "order": [
                {
                    "column": 0,
                    "dir": "desc"
                }
            ],
            "start": 0,
            "length": 20,
            "search": {
                "value": ""
            },
            "categoryType": "sku_category"
        }

        r = requests.post(url=url, json=body, headers=headers)

        # print(r.json()["data"]["data"]["data"])
        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_07_CreateSku(self):
        url = host + ":" + port + "/sku/create"
        sku_name = "SKU_" + str(random.randint(10, 99999))
        self.g['Global_sku_name'] = sku_name
        sku_id = "ID10001" + str(random.randint(10, 99999))

        body = {
            "name": sku_name,
            "sku": sku_id,
            "sku_type": "common",
            "sku_category_id": self.g['CategoryId'],
            "sku_sub_category_id": self.g['SubCategoryId'],
            "suggested_price": "22",
            "cost": "22",
            "supplier_id": 8,
            "sku_uom_id": self.g['UOMId'],
            "sku_uom_name": self.g['UOMName'],
            "skuSecondaryUomList": [
                {
                    "secondary_uom_id": 5,
                    "secondary_uom_name": "TRAY",
                    "val": "20"
                }, {
                    "secondary_uom_id": 6,
                    "secondary_uom_name": "BOX",
                    "val": "30"
                }
            ],
            "threshold": 2000,
            "hashtag": "SKU TEST2",
            "barcode": ["17456 SDF23J XXX"],
            "remark": "new sku 2",
            "status": "New",
            "created_by": "super",
            "updated_by": "super"
        }

        r = requests.post(url=url, json=body, headers=headers)

        sku_code_id = r.json()["data"]["insertId"]

        # Assert
        self.g['SkuCodeId'] = sku_code_id
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_08_SearchSkuDetail(self):
        url = host + ":" + port + "/sku/details/" + str(self.g['SkuCodeId'])

        r = requests.get(url=url, headers=headers)
        sku_detail_name = r.json()['data']['name']
        sku_detail_sku = r.json()['data']['sku']
        sku_detail_barcode = r.json()['data']['barcode']

        self.g['SkuDetailSku'] = sku_detail_sku
        self.g['SkuDetailBarcode'] = sku_detail_barcode

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")
        self.assertEqual(sku_detail_name, self.g['Global_sku_name'])

    def test_09_SkuList(self):
        url = host + ":" + port + "/sku/list"

        body = {
            "draw": 1,
            "columns": [
                {
                    "data": "created_time",
                    "name": "",
                    "searchable": "true",
                    "orderable": "true",
                    "search": {
                        "value": "",
                        "regex": "false"
                    }
                }
            ],
            "order": [
                {
                    "column": 0,
                    "dir": "asc"
                }
            ],
            "start": 0,
            "length": 20,
            "search": {
                "value": ""
            }
        }

        r = requests.post(url=url, json=body, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_10_NewRR(self):
        url = host + ":" + port + "/receivingReport/create"

        body = {
            "supplier_id": 14,
            "warehouse_id": 25,
            "expected_data": "2020-04-29",
            "is_incoming": 0,
            "detail_list": [{
                "sku_id": self.g['SkuCodeId'],
                "uom_quantity": 100,
                "uom": self.g['UOMId'],
                "cost": 1,
                "sub_total": 100,
                "gst": 7,
                "total_amount": 107
            }],
            "supplier_contact": {
                "type_id": 18,
                "address": "test",
                "country": "China",
                "postal_code": "441300",
                "contact_person": "test",
                "contact_no": "965-24ui43"
            },
            "delivered_contact": {
                "type_id": 13,
                "address": "test",
                "country": "China",
                "postal_code": "441300",
                "contact_person": "test",
                "contact_no": ""
            },
            "bill_contact": {
                "type_id": 19,
                "address": "test",
                "country": "China",
                "postal_code": "441300",
                "contact_person": "test",
                "contact_no": ""
            },
            "is_submit": 1  # 0 is save， 1 is submit
        }

        r = requests.post(url=url, json=body, headers=headers)

        rr_id = r.json()['data']['id']['insertId']
        self.g['RR_ID'] = rr_id

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_11_RRDetails(self):
        url = host + ":" + port + "/receivingReport/detail"

        params = {"id": self.g['RR_ID']}

        r = requests.get(url=url, params=params, headers=headers)

        work_id = r.json()['data']['work_id']
        self.g['G_work_ID'] = work_id
        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_12_SearchRRInPages(self):
        url = host + ":" + port + "/receivingReport/page"

        r = requests.get(url=url, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_13_FlowUpdateApproved(self):
        url = host + ":" + port + "/work/update"

        body = {
            "work_id": self.g['G_work_ID'],
            "role_id": 1,
            "result": 10,
            "remark": "审核通过"
        }

        r = requests.put(url=url, json=body, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_14_SearchViaFlowID(self):
        url = host + ":" + port + "/work/findById"

        params = {"id": self.g['G_work_ID']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_15_SearchSkuInventory(self):
        url = host + ":" + port + "/inventory/findSkuInventory"

        params = {"sku_id": self.g['SkuCodeId']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_16_GetSkuDetailsViaSkuId(self):
        url = host + ":" + port + "/srf/sku/detail"

        params = {"id": self.g['SkuCodeId'], "warehouse_id": "25"}

        r = requests.get(url=url, params=params, headers=headers)

        self.g['CurrentStock'] = r.json()['data']['current_stock']
        print(self.g['CurrentStock'])

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_17_NewSRF(self):
        url = host + ":" + port + "/srf/create"

        body = {
            "urgency": "low",
            "fromList": {
                "id": 25,
                "location": "Primary Warehouse",
                "address": "test",
                "country": "China",
                "postal_code": "441300",
                "contact_person": "test",
                "contact_no": ""
            },
            "toList": {
                "id": 24,
                "location": "OutletA",
                "address": "test",
                "country": "China",
                "postal_code": "441300",
                "contact_person": "test",
                "contact_no": ""
            },
            "skuList": [{
                "sku": self.g['SkuDetailSku'],
                "sku_id": self.g['SkuCodeId'],
                "sku_name": self.g['Global_sku_name'],
                "sku_barcode": self.g['SkuDetailBarcode'],
                "uom_quantity": 5,
                "current_stock": self.g['CurrentStock'],
                "uom": self.g['UOMId'],
                "remark": "test srf",
                "uom_name": self.g['UOMName'],
                "cost": 5
            }],
            "to_type": "Outlet",
            "receive_time": "2020-04-09",
            "is_submit": 1,
            "sku_count": 1,
            "request_by": "super"
        }

        r = requests.post(url=url, json=body, headers=headers)

        self.g['SrfID'] = r.json()['data']['insertId']
        print(r.json())
        print(self.g['SrfID'])

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_18_GetSRFDetails(self):
        url = host + ":" + port + "/srf/detail/" + str(self.g['SrfID'])

        r = requests.get(url=url, headers=headers)

        self.g['SRFWorkId'] = r.json()['data']['workId']

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_19_SearchFlowInPages(self):
        url = host + ":" + port + "/work/page"

        body = {
            "draw": 1,
            "columns": [
                {
                    "data": "updated_time",
                    "name": "",
                    "searchable": "true",
                    "orderable": "true",
                    "search": {
                        "value": "",
                        "regex": "false"
                    }
                }
            ],
            "order": [
                {
                    "column": 0,
                    "dir": "desc"
                }
            ],
            "start": 0,
            "length": 29,
            "search": {
                "value": ""
            },
            "role_id": 1,
            "status": "10",
            "flow": ""
        }

        r = requests.post(url=url, json=body, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_20_FlowUpdateApproved(self):
        url = host + ":" + port + "/work/update"

        body = {
            "work_id": self.g['SRFWorkId'],
            "role_id": 1,
            "result": 10,
            "remark": "审核通过"
        }

        r = requests.put(url=url, json=body, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_21_SearchViaFlowID(self):
        url = host + ":" + port + "/work/findById"

        params = {"id": self.g['SRFWorkId']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_22_SearchSkuInventory(self):
        url = host + ":" + port + "/inventory/findSkuInventory"

        params = {"sku_id": self.g['SkuCodeId']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_23_NewSAR(self):
        url = host + ":" + port + "/stockAdjustment/create"

        body = {
            "is_submit": 1,
            "detail_list": [{
                "sku": self.g['SkuDetailSku'],
                "sku_id": self.g['SkuCodeId'],
                "sku_name": self.g['Global_sku_name'],
                "sku_barcode": self.g['SkuDetailBarcode'],
                "adj_qty": -5,
                "adj_value": 200,
                "adj_total_value": 1000,
                "uom": self.g['UOMId'],
                "uom_name": self.g['UOMName'],
                "uom_quantity": -5,
                "reason": "",
                "remark": "OK"
            }],
            "warehouse_id": 25
        }

        r = requests.post(url=url, json=body, headers=headers)

        self.g['SarID'] = r.json()['data']['insertId']

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_24_SearchSARInPages(self):
        url = host + ":" + port + "/stockAdjustment/page"

        body = {
            "draw": 1,
            "columns": [
                {
                    "data": "updated_time",
                    "name": "",
                    "searchable": "true",
                    "orderable": "true",
                    "search": {
                        "value": "",
                        "regex": "false"
                    }
                }
            ],
            "order": [
                {
                    "column": 0,
                    "dir": "desc"
                }
            ],
            "start": 0,
            "length": 9,
            "search": {
                "value": ""
            },
            "status": "",
            "warehouse_id": "null",
            "begin_date": "2020-04-10",
            "end_date": "2020-04-21"
        }

        r = requests.post(url=url, json=body, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_25_SearchSARViaId(self):
        url = host + ":" + port + "/stockAdjustment/detail"

        params = {"id": self.g['SarID']}

        r = requests.get(url=url, params=params, headers=headers)

        self.g['SarWordID'] = r.json()['data']['workId']

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_26_FlowUpdateApproved(self):
        url = host + ":" + port + "/work/update"

        body = {
            "work_id": self.g['SarWordID'],
            "role_id": 1,
            "result": 10,
            "remark": "审核通过"
        }

        r = requests.put(url=url, json=body, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_27_SearchViaFlowID(self):
        url = host + ":" + port + "/work/findById"

        params = {"id": self.g['SarWordID']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_28_SearchSkuInventory(self):
        url = host + ":" + port + "/inventory/findSkuInventory"

        params = {"sku_id": self.g['SkuCodeId']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_29_GetAverageCostHistory(self):
        url = host + ":" + port + "/inventory/getCostHistory"

        params = {"sku_id": self.g['SkuCodeId'], "report_type": "day"}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")

    def test_30_GetSKUInventoryDetails(self):
        url = host + ":" + port + "/inventory/getInventoryDetail"

        params = {"sku_id": self.g['SkuCodeId']}

        r = requests.get(url=url, params=params, headers=headers)

        # Assert
        self.assertEqual(200, r.status_code, "Code should be 200!")


# Run test suite, select test case and add them in test suite, testing the test case and report result
if __name__ == '__main__':
    suite = unittest.TestSuite()
    # select the test case to run
    suite.addTest(SCMScenarioOneTest("Test_01_SignIn"))  # select the test case
    suite.addTest(SCMScenarioOneTest("test_02_NewUom"))
    suite.addTest(SCMScenarioOneTest("test_03_SearchUom"))
    suite.addTest(SCMScenarioOneTest("test_04_NewCategory"))
    suite.addTest(SCMScenarioOneTest("test_05_NewSubCategory"))
    suite.addTest(SCMScenarioOneTest("test_06_SearchCategoryInPages"))
    suite.addTest(SCMScenarioOneTest("test_07_CreateSku"))
    suite.addTest(SCMScenarioOneTest("test_08_SearchSkuDetail"))
    suite.addTest(SCMScenarioOneTest("test_09_SkuList"))
    suite.addTest(SCMScenarioOneTest("test_10_NewRR"))
    suite.addTest(SCMScenarioOneTest("test_11_RRDetails"))
    suite.addTest(SCMScenarioOneTest("test_12_SearchRRInPages"))
    suite.addTest(SCMScenarioOneTest("test_13_FlowUpdateApproved"))
    suite.addTest(SCMScenarioOneTest("test_14_SearchViaFlowID"))
    suite.addTest(SCMScenarioOneTest("test_15_SearchSkuInventory"))
    suite.addTest(SCMScenarioOneTest("test_16_GetSkuDetailsViaSkuId"))
    suite.addTest(SCMScenarioOneTest("test_17_NewSRF"))
    suite.addTest(SCMScenarioOneTest("test_18_GetSRFDetails"))
    suite.addTest(SCMScenarioOneTest("test_19_SearchFlowInPages"))
    suite.addTest(SCMScenarioOneTest("test_20_FlowUpdateApproved"))
    suite.addTest(SCMScenarioOneTest("test_21_SearchViaFlowID"))
    suite.addTest(SCMScenarioOneTest("test_22_SearchSkuInventory"))
    suite.addTest(SCMScenarioOneTest("test_23_NewSAR"))
    suite.addTest(SCMScenarioOneTest("test_24_SearchSARInPages"))
    suite.addTest(SCMScenarioOneTest("test_25_SearchSARViaId"))
    suite.addTest(SCMScenarioOneTest("test_26_FlowUpdateApproved"))
    suite.addTest(SCMScenarioOneTest("test_27_SearchViaFlowID"))
    suite.addTest(SCMScenarioOneTest("test_28_SearchSkuInventory"))
    suite.addTest(SCMScenarioOneTest("test_29_GetAverageCostHistory"))
    suite.addTest(SCMScenarioOneTest("test_30_GetSKUInventoryDetails"))

    # Report the result after run the test case
    with(open('./result.html', 'wb')) as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='The SCM_Lite API test report',
            description='Run the SCM_Lite Basic flow testing'
        )
        runner.run(suite)
    #      ***the step by step to report the result***
    # filename = "D:\\Course\\Script\\SCM_Lite\\result.html"
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="The is the test report!")
    # runner.run(suite)
    # fp.close()
