code = "789CC593CD8E9B301080EF3CC5341783761BC162B6BB9172401B0E4869A836E9A1A795C143E40A30B28D549EAB8FD017AB17363FF492B45AA99610B6C7FAF4CD8C2DEA562A0339D3784F9D52C91A840431EE6E8D12CD3ECD9CB7B5EEB5E318D52F001CB083698D769BC49B6CF3ED73F675FB92AE088806F695CC59A55DEF16C8A7C80F7CC68A20A28CD29005C1C36358B228E2819FB3479F4C58E728F8B004A24DC7B131E4322920701C13BD82D5B96035EB3B3DD871A1AE300B7D7242C98ABF68C3656760F95A86F9B81862A7A58DD5FD717AA89EEB9DDB9CC9B8E4896923AA8A116FB92445BCDDA5EB757C39D5B024D31427D064B35368B0115C0E5C5BBDE764976CD2557625FACF0A4EF05FE45A24FC7964B75995E24ABD0BB8603A1EA04FF196FD2D70D284B36E1DE2ADED857167A683E2D74F2EF612388242DD76A80D03D40B98C10D68A3DCF12DCCF37B8A4D2139BA796F50BBE737F386444518D28872724B3A537E7C209E37E7381CF73CCFC11F05B6F6360F690AD9244A4965B3065C0C3AAF8FC8395CD64BEE23EC74BEB5D5FB97C4F024B6EB5BFCAF4E177AFB7D76507D27B76BBDA84FEFEECAB2B4FFD27AD9CFA747AFD20F661EC06F70B081BB" 
import base64
import zlib
def run(code,globals,locals): exec(zlib.decompress(base64.b16decode(code)),globals,locals)
def assert_control(globals,locals):
    run(code,globals,locals)