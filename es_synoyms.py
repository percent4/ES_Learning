# -*- coding: utf-8 -*-
import json

from elasticsearch import Elasticsearch

# 创建 Elasticsearch 客户端实例，连接到本地的 Elasticsearch 服务
es = Elasticsearch("http://localhost:9200")

# 定义同义词集的 ID
set_id = "python_synonyms_test"
# 定义同义词规则的 ID
rule_id = "rule1"


# 查看同义词集列表
def list_synonym_sets():
    try:
        response = es.transport.perform_request(method="GET", url="/_synonyms")
        print("\n同义词集列表:")
        print(response)
    except Exception as e:
        print(f"\n获取同义词集列表时出错: {e}")


# 查看特定同义词集的详细信息
def get_synonym_set(set_id):
    try:
        response = es.transport.perform_request("GET", f"/_synonyms/{set_id}")
        print(f"\n同义词集 '{set_id}' 的详细信息:")
        print(response)
    except Exception as e:
        print(f"\n获取同义词集 '{set_id}' 时出错: {e}")


# 查看特定同义词规则
def get_synonym_rule(set_id, rule_id):
    try:
        response = es.transport.perform_request("GET", f"/_synonyms/{set_id}/{rule_id}")
        print(f"\n同义词集 '{set_id}' 中规则 '{rule_id}' 的详细信息:")
        print(response)
    except Exception as e:
        print(f"\n获取同义词规则 '{rule_id}' 时出错: {e}")


# 更新同义词集
def update_synonym_set(set_id, synonyms_payload):
    try:
        response = es.transport.perform_request(method="PUT",
                                                url=f"/_synonyms/{set_id}",
                                                headers={"Content-Type": "application/json"},
                                                body=synonyms_payload)
        print(f"\n同义词集 '{set_id}' 更新成功:")
        print(response)
    except Exception as e:
        print(f"\n更新同义词集 '{set_id}' 时出错: {e}")


# 更新特定同义词规则
def update_synonym_rule(set_id, rule_id, synonym_rule):
    try:
        response = es.transport.perform_request(method="PUT",
                                                url=f"/_synonyms/{set_id}/{rule_id}",
                                                headers={"Content-Type": "application/json"},body=synonym_rule)
        print(f"\n同义词集 '{set_id}' 中规则 '{rule_id}' 更新成功:")
        print(response)
    except Exception as e:
        print(f"\n更新同义词规则 '{rule_id}' 时出错: {e}")


# 示例同义词集的定义
synonyms_payload = {
    "synonyms_set": [
        {
            "id": "rule1",
            "synonyms": "自行车,脚踏车"
        },
        {
            "id": "rule2",
            "synonyms": "手机,移动电话"
        }
        # 可以添加更多的同义词规则
    ]
}

# 示例同义词规则的定义
synonym_rule = {
    "synonyms": "自行车,脚踏车,单车"
}

# 调用函数示例
if __name__ == "__main__":
    # 查看同义词集列表
    list_synonym_sets()
    # 更新同义词集
    update_synonym_set(set_id, synonyms_payload)
    # 查看更新同义词集后的列表
    print("\n更新后的同义词集列表:")
    list_synonym_sets()

    # 查看特定同义词集
    get_synonym_set(set_id)

    # 查看特定同义词规则
    get_synonym_rule(set_id, rule_id)
    # 更新特定同义词规则
    update_synonym_rule(set_id, rule_id, synonym_rule)
    # 查看更新后的特定同义词规则
    print(f"{set_id}中的{rule_id}更新后的同义词规则:")
    get_synonym_rule(set_id, rule_id)
