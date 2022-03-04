#
import os

import requests as requests
from utilities.utils import get_auth


def payload_gl00201_sub(self, period):
    url = 'https://fa-epxv-test-saasfaprod1.fa.ocs.oraclecloud.com/xmlpserver/services/ExternalReportWSSService?wsdl'
    # username = 'ita_dev'
    # password = '!QAZ2wsx'
    # self.url = get_url()
    self.period = period
    self.str_auth = get_auth()

    payload_gl00201 = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:pub="http://xmlns.oracle.com/oxp/service/PublicReportService">
       <soap:Header/>
       <soap:Body>
          <pub:runReport>
             <pub:reportRequest>
                <pub:attributeFormat>excel</pub:attributeFormat>
                <pub:parameterNameValues>
                   <pub:item>
                      <pub:name>P_LEDGER</pub:name>
                      <pub:values>
                         <pub:item>基本</pub:item>
                      </pub:values>
                   </pub:item>
                   <pub:item>
                      <pub:name>P_PERIOD</pub:name>
                      <pub:values>
                         <pub:item>2020-03</pub:item>
                      </pub:values>
                   </pub:item>
                   <pub:item>
                      <pub:name>P_JOURNAL_CLASS</pub:name>
                      <pub:values>
                         <pub:item>T</pub:item>
                      </pub:values>
                   </pub:item>
                </pub:parameterNameValues>
                <pub:reportAbsolutePath>/Custom/XXGL/GL00201 - 各課照合リスト ALL.xdo</pub:reportAbsolutePath>
                <pub:sizeOfDataChunkDownload>-1</pub:sizeOfDataChunkDownload>
             </pub:reportRequest>
          </pub:runReport>
       </soap:Body>
    </soap:Envelope>"""

    headers = {
        'Content-Type': 'application/soap+xml;charset=UTF-8',
        'Authorization': 'Basic aXRhX2RldjohUUFaMndzeA=='
    }
    response = requests.post(url, headers=headers, data=payload_gl00201.encode("utf-8"))
    self.xml_txt = response.text
    str_begin = self.xml_txt.find("<ns2:reportBytes>")
    str_end = self.xml_txt.find("</ns2:reportBytes>")
    str_file = self.xml_txt[(str_begin + len("<ns2:reportBytes>")):str_end]

    outfile = os.path.join(BASE_DIR, 'media', 'excel_holder', 'gl00201.xls')
    res = convert_b64_string_to_file(self, str_file, outfile)
    # print(res)
    return res
