{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "MongoDB실습(1)의 사본",
      "provenance": [],
      "authorship_tag": "ABX9TyM3o9AfS1+wEhZitHI0s9PH"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-cCCc7FaZDWy"
      },
      "outputs": [],
      "source": [
        "mongo_path = 'mongodb+srv://sehyun:Tpgus343!@cluster0.txbgo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pymongo import MongoClient # mongoDB 접속을 비롯한 엑셀을 할 때 사용하는 라이브러리"
      ],
      "metadata": {
        "id": "GNQF82GBbUvq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import requests #python file에서 접속이 필요할 때 사용하는 라이브러리"
      ],
      "metadata": {
        "id": "Ms25bv8TbU5R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd #dataframe 단위 작업을 할 때 사용하는 라이브러리(이번 수업 필요 x)"
      ],
      "metadata": {
        "id": "Wf6I5MSEbU9K"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#! pip install pymongo[srv]"
      ],
      "metadata": {
        "id": "qtj3ZxSBfTr7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "client = MongoClient(mongo_path)"
      ],
      "metadata": {
        "id": "3JhLJ2CodLeN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "client"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wbGeqHuSdvsL",
        "outputId": "48dcb1a6-d309-4f15-91e0-d29cbce92396"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "MongoClient(host=['cluster0-shard-00-02.txbgo.mongodb.net:27017', 'cluster0-shard-00-00.txbgo.mongodb.net:27017', 'cluster0-shard-00-01.txbgo.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority', authsource='admin', replicaset='atlas-v73sul-shard-0', tls=True)"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "client.Cluster0.list_collection_names()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vToCua0Udvwj",
        "outputId": "b8abdee4-dda6-42bb-a129-e3206ddbc9d5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['users']"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "db = client.Cluster0"
      ],
      "metadata": {
        "id": "7rbsuH2Bdvy5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "new_collection = db.posts"
      ],
      "metadata": {
        "id": "aTBSG3v9dv1P"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "new_collection.insert_one({'title':'hello, mongo', 'content':'Hello, all!'}) #하나만 출력할거기에 one"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2bLf5eQMdwJ1",
        "outputId": "0ae0d9dd-bed4-472b-cd23-8646f4f8ae3e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pymongo.results.InsertOneResult at 0x7f0001c05640>"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "db.list_collection_names()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g0zGcXOJdwML",
        "outputId": "aa0bd51d-54fe-4905-9ed7-99334aaea015"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['posts', 'users']"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query ={}\n",
        "db.posts.find_one(query) #db의 첫번째 부분을 가져온다.위의 Insert_one 한 데이터가 나온다"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ETtPcJd6pKiq",
        "outputId": "aaa7a085-8810-4d88-cef6-e94c32d0d1c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'_id': ObjectId('624bf0c0a836b35c1f131631'),\n",
              " 'content': 'Hello, all!',\n",
              " 'title': 'hello, mongo'}"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "many_posts = [\n",
        "              \n",
        "  {'title': 'post 1', 'content': 'this is post 1'},\n",
        "  {'title': 'post 2', 'content': 'this is post 2'},\n",
        "  {'title': 'post 3', 'content': 'this is post 3'}\n",
        "]"
      ],
      "metadata": {
        "id": "kIlbljzJps3T"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "new_collection.insert_many(many_posts) #여러 개를 출력하려고 하기에 many\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_a2MwG6Pps5V",
        "outputId": "a5e02b9f-4415-4fdd-d467-260e70b391bf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pymongo.results.InsertManyResult at 0x7f0001c6a640>"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query={}\n",
        "cursor = new_collection.find(query) #검색 결과를 cursor에 할당"
      ],
      "metadata": {
        "id": "RjGHEOo2ph6w"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "[item for item in cursor] #cursor 안에 있는 것들이 여러 개 이기에  리스트 형식으로 하나씩 뽑기, 리스트 컴프리헨션"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ml1-ngp-qvXz",
        "outputId": "7d55f992-7d53-403a-df5f-2305863557f2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bf0c0a836b35c1f131631'),\n",
              "  'content': 'Hello, all!',\n",
              "  'title': 'hello, mongo'},\n",
              " {'_id': ObjectId('624bf22ca836b35c1f131632'),\n",
              "  'content': 'this is post 1',\n",
              "  'title': 'post 1'},\n",
              " {'_id': ObjectId('624bf22ca836b35c1f131633'),\n",
              "  'content': 'this is post 2',\n",
              "  'title': 'post 2'},\n",
              " {'_id': ObjectId('624bf22ca836b35c1f131634'),\n",
              "  'content': 'this is post 3',\n",
              "  'title': 'post 3'}]"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#리스트 컴프리헨션을 안 쓸 경우\n",
        "#new_list = []\n",
        "#for item in cursor:\n",
        "#   new_list.append(item)   "
      ],
      "metadata": {
        "id": "HULIVerLrDU8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "user_collec = db.users"
      ],
      "metadata": {
        "id": "yX7NHkyWssWv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "many_users = [\n",
        "  {'name':\"John Doe\", 'email':\"jd@gmail.com\"},\n",
        "  {'name':\"Jane Doe\", 'email':\"jane@gmai.com\"},\n",
        "  {'name':\"Gil-dong Hong\", 'email':\"gdhong@naver.com\"},\n",
        "]#trailing comma: 마지막 자료의 뒤에 붙는 쉼표"
      ],
      "metadata": {
        "id": "tKBl16JDssY9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "user_collec.insert_many(many_users)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bWxnaQ5Jssb1",
        "outputId": "f7e3e2d1-600f-48b0-8ee5-aa677e3f475b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pymongo.results.InsertManyResult at 0x7f000006ce10>"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = {}\n",
        "cursor = user_collec.find(query) #전체 내용을 query에 넣어라"
      ],
      "metadata": {
        "id": "dJHe8V05xKur"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "[item for item in cursor]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h2msqi3BxK0O",
        "outputId": "6353d01b-2491-420c-c48e-6fc0e5de8be1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bf8faa836b35c1f131635'),\n",
              "  'email': 'jd@gmail.com',\n",
              "  'name': 'John Doe'},\n",
              " {'_id': ObjectId('624bf8faa836b35c1f131636'),\n",
              "  'email': 'jane@gmai.com',\n",
              "  'name': 'Jane Doe'},\n",
              " {'_id': ObjectId('624bf8faa836b35c1f131637'),\n",
              "  'email': 'gdhong@naver.com',\n",
              "  'name': 'Gil-dong Hong'}]"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = {\n",
        "    \"name\":'John Doe'\n",
        "}\n",
        "cursor = user_collec.find(query) #특정 내용을 query에 넣어라\n",
        "[item for item in cursor] #조건에 일치하는 자료만 나오라"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h87CzByTxK2J",
        "outputId": "472d7102-9ee1-46a4-d04b-e1fb38e4c78d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bf8faa836b35c1f131635'),\n",
              "  'email': 'jd@gmail.com',\n",
              "  'name': 'John Doe'}]"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = {\n",
        "    'email':'jane@gmai.com'\n",
        "}\n",
        "cursor = user_collec.find(query) #특정 내용을 query에 넣어라\n",
        "\n",
        "[item for item in cursor]#조건에 일치하는 자료만 나오라"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m5HyqQRIxK6l",
        "outputId": "a96c0e58-081d-487d-8904-34d1c2e415da"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bf8faa836b35c1f131636'),\n",
              "  'email': 'jane@gmai.com',\n",
              "  'name': 'Jane Doe'}]"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#mongodb ref\n",
        "#stackoverflow\n",
        "#위의 두 개를 참고하여서 과제하기"
      ],
      "metadata": {
        "id": "Ca2XhRA2xK9c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#이름이 홍길동이고 이메일도 같은지\n",
        "query = {\n",
        "    \"name\":'Gil-dong Hong', 'email':'gdhong@naver.com'\n",
        "\n",
        "}\n",
        "cursor = user_collec.find(query)\n",
        "[item for item in cursor]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d2ETR9vBxLBW",
        "outputId": "283065d6-a215-4ba3-839f-118e2fed720e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bf8faa836b35c1f131637'),\n",
              "  'email': 'gdhong@naver.com',\n",
              "  'name': 'Gil-dong Hong'}]"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = {\n",
        "    '$or': [\n",
        "         {'name':'John Doe'},\n",
        "          {'email':\"jane@gmai.com\"}\n",
        "    ]\n",
        "}\n",
        "\n",
        "cursor = user_collec.find(query)\n",
        "[item for item in cursor]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aYkAT2g0zlsg",
        "outputId": "ef23f6dc-a951-427c-a3ff-666860dc6a51"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bf8faa836b35c1f131635'),\n",
              "  'email': 'jd@gmail.com',\n",
              "  'name': 'John Doe'},\n",
              " {'_id': ObjectId('624bf8faa836b35c1f131636'),\n",
              "  'email': 'jane@gmai.com',\n",
              "  'name': 'Jane Doe'}]"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "many_users = [\n",
        "  {'name':\"John Doe\", 'email':\"jd@gmail.com\",\"age\":30},\n",
        "  {'name':\"Jane Doe\", 'email':\"jane@gmai.com\",\"age\":20},\n",
        "  {'name':\"Gil-dong Hong\", 'email':\"gdhong@naver.com\",\"age\":10},\n",
        "]#trailing comma: 마지막 자료의 뒤에 붙는 쉼표\n",
        "\n",
        "user_collec.insert_many(many_users)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V5XgDXPH01Z3",
        "outputId": "27ebe2d7-8fb3-4c97-fbbf-6328ebaf2b92"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pymongo.results.InsertManyResult at 0x7f0001bf9f00>"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "[item for item in user_collec.find({})]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1zH-1iUr01b4",
        "outputId": "e96f1ec2-7848-4042-db0c-90e9ae90ee3a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bf8faa836b35c1f131635'),\n",
              "  'email': 'jd@gmail.com',\n",
              "  'name': 'John Doe'},\n",
              " {'_id': ObjectId('624bf8faa836b35c1f131636'),\n",
              "  'email': 'jane@gmai.com',\n",
              "  'name': 'Jane Doe'},\n",
              " {'_id': ObjectId('624bf8faa836b35c1f131637'),\n",
              "  'email': 'gdhong@naver.com',\n",
              "  'name': 'Gil-dong Hong'},\n",
              " {'_id': ObjectId('624bfd34a836b35c1f131638'),\n",
              "  'age': 30,\n",
              "  'email': 'jd@gmail.com',\n",
              "  'name': 'John Doe'},\n",
              " {'_id': ObjectId('624bfd34a836b35c1f131639'),\n",
              "  'age': 20,\n",
              "  'email': 'jane@gmai.com',\n",
              "  'name': 'Jane Doe'},\n",
              " {'_id': ObjectId('624bfd34a836b35c1f13163a'),\n",
              "  'age': 10,\n",
              "  'email': 'gdhong@naver.com',\n",
              "  'name': 'Gil-dong Hong'}]"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = {\n",
        "    'age':{'$gte':20}\n",
        "}\n",
        "\n",
        "cursor = user_collec.find(query)\n"
      ],
      "metadata": {
        "id": "-mBB-GKi01eg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "[item for item in cursor]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JuBl_80q162I",
        "outputId": "c5392087-77c1-4891-8fe4-7f3cd7b31c4d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624bfd34a836b35c1f131638'),\n",
              "  'age': 30,\n",
              "  'email': 'jd@gmail.com',\n",
              "  'name': 'John Doe'},\n",
              " {'_id': ObjectId('624bfd34a836b35c1f131639'),\n",
              "  'age': 20,\n",
              "  'email': 'jane@gmai.com',\n",
              "  'name': 'Jane Doe'}]"
            ]
          },
          "metadata": {},
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n"
      ],
      "metadata": {
        "id": "5FQ7ghn22XnQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response = requests.get('http://www.google.com/')"
      ],
      "metadata": {
        "id": "1kQjVTav2Xpz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response.status_code"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7oGf60NV2Xtc",
        "outputId": "dbbe25d3-f0c5-4dd8-879d-b02d6bdab0ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "200"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 72
        },
        "id": "3G7m4okV2XzM",
        "outputId": "4cb0b329-b066-4b36-871a-335d87a3c197"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'<!doctype html><html itemscope=\"\" itemtype=\"http://schema.org/WebPage\" lang=\"en\"><head><meta content=\"Search the world\\'s information, including webpages, images, videos and more. Google has many special features to help you find exactly what you\\'re looking for.\" name=\"description\"><meta content=\"noodp\" name=\"robots\"><meta content=\"text/html; charset=UTF-8\" http-equiv=\"Content-Type\"><meta content=\"/images/branding/googleg/1x/googleg_standard_color_128dp.png\" itemprop=\"image\"><title>Google</title><script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){window.google={kEI:\\'V_9LYs33MvqYwbkPya-iuA8\\',kEXPI:\\'0,1302536,56873,6058,207,2414,2390,2316,383,246,5,1353,4014,1237,1122516,1197744,657,380089,16115,17444,1954,9286,17572,4859,996,365,9291,3027,17581,4020,978,13228,8039,6430,22741,261,4820,1593,1279,2742,149,1103,840,1983,214,4100,108,3406,606,2023,1777,520,14670,3227,2845,7,5599,11851,16320,1851,15324,432,3,1590,1,5444,149,11323,2652,4,1528,655,1649,923,6116,22023,3050,2658,7357,30,13628,2980,1457,9358,5993,1435,5815,2542,4094,4052,3,3541,1,14711,2096,25347,2,14022,1931,442,342,255,2993,1557,744,5852,10463,1160,5679,1020,2380,2719,16549,1748,1,8,7718,4568,6255,6720,1,16700,830,422,5835,14967,1539,2794,2204,2083,390,1412,1395,445,2,2,1,6395,4561,13823,1418,10,1,346,78,8155,113,6469,316,252,231,2,3,182,2,1290,970,594,5213,2215,421,880,1972,936,6550,791,4447,174,1449,3,1,6056,1144,1410,914,415,371,184,358,231,3129,868,933,504,1249,968,745,610,54,750,25,73,2153,13,241,1720,95,740,665,557,590,71,232,110,84,2765,327,17,801,335,230,444,506,1,211,1190,445,57,338,2,89,2798,401,151,5445491,3892,1196,121,8796694,882,444,3,1877,1,2562,1,748,141,795,563,1,4265,1,1,2,1331,4142,2609,155,17,13,72,139,4,2,20,2,169,13,19,46,5,39,96,548,29,2,2,1,2,1,2,2,7,4,1,2,2,2,2,2,2,353,513,186,1,1,158,3,2,2,2,2,2,4,2,3,3,269,1601,141,1002,71,241,126,7,2,13,2,2,5,1,5,3,24,23951477,2862026,1176548,3,3112,3,450,1964,2935,159,1358,4726,3,2664,4828,2554,956,9\\',kBL:\\'zIb2\\'};google.sn=\\'webhp\\';google.kHL=\\'en\\';})();(function(){\\nvar f=this||self;var h,k=[];function l(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute(\"eid\")));)a=a.parentNode;return b||h}function m(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute(\"leid\")));)a=a.parentNode;return b}\\nfunction n(a,b,c,d,g){var e=\"\";c||-1!==b.search(\"&ei=\")||(e=\"&ei=\"+l(d),-1===b.search(\"&lei=\")&&(d=m(d))&&(e+=\"&lei=\"+d));d=\"\";!c&&f._cshid&&-1===b.search(\"&cshid=\")&&\"slh\"!==a&&(d=\"&cshid=\"+f._cshid);c=c||\"/\"+(g||\"gen_204\")+\"?atyp=i&ct=\"+a+\"&cad=\"+b+e+\"&zx=\"+Date.now()+d;/^http:/i.test(c)&&\"https:\"===window.location.protocol&&(google.ml&&google.ml(Error(\"a\"),!1,{src:c,glmm:1}),c=\"\");return c};h=google.kEI;google.getEI=l;google.getLEI=m;google.ml=function(){return null};google.log=function(a,b,c,d,g){if(c=n(a,b,c,d,g)){a=new Image;var e=k.length;k[e]=a;a.onerror=a.onload=a.onabort=function(){delete k[e]};a.src=c}};google.logUrl=n;}).call(this);(function(){\\ngoogle.y={};google.sy=[];google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.sx=function(a){google.sy.push(a)};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};google.bx=!1;google.lx=function(){};}).call(this);google.f={};(function(){\\ndocument.documentElement.addEventListener(\"submit\",function(b){var a;if(a=b.target){var c=a.getAttribute(\"data-submitfalse\");a=\"1\"===c||\"q\"===c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener(\"click\",function(b){var a;a:{for(a=b.target;a&&a!==document.documentElement;a=a.parentElement)if(\"A\"===a.tagName){a=\"1\"===a.getAttribute(\"data-nohref\");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}\\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#1558d6}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#4b11a8;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#1558d6}a:visited{color:#4b11a8}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#f8f9fa;border:solid 1px;border-color:#dadce0 #70757a #70757a #dadce0;height:30px}.lsbb{display:block}#WqQANb a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#dadce0}.lst:focus{outline:none}</style><script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){window.google.erd={jsr:1,bv:1555,de:true};\\nvar f=this||self;var g,h=null!=(g=f.mei)?g:1,m,n=null!=(m=f.sdo)?m:!0,p=0,q,r=google.erd,u=r.jsr;google.ml=function(a,b,d,k,c){c=void 0===c?2:c;b&&(q=a&&a.message);if(google.dl)return google.dl(a,c,d),null;if(0>u){window.console&&console.error(a,d);if(-2===u)throw a;b=!1}else b=!a||!a.message||\"Error loading script\"===a.message||p>=h&&!k?!1:!0;if(!b)return null;p++;d=d||{};var e=c;c=encodeURIComponent;b=\"/gen_204?atyp=i&ei=\"+c(google.kEI);google.kEXPI&&(b+=\"&jexpid=\"+c(google.kEXPI));b+=\"&srcpg=\"+c(google.sn)+\"&jsr=\"+c(r.jsr)+\"&bver=\"+c(r.bv)+(\"&jsel=\"+e);e=a.lineNumber;void 0!==e&&(b+=\"&line=\"+\\ne);var l=a.fileName;l&&(b+=\"&script=\"+c(l),e&&l===window.location.href&&(e=document.documentElement.outerHTML.split(\"\\\\n\")[e],b+=\"&cad=\"+c(e?e.substring(0,300):\"No script found.\")));for(var t in d)b+=\"&\",b+=c(t),b+=\"=\",b+=c(d[t]);b=b+\"&emsg=\"+c(a.name+\": \"+a.message);b=b+\"&jsst=\"+c(a.stack||\"N/A\");12288<=b.length&&(b=b.substr(0,12288));a=b;k||google.log(0,\"\",a);return a};window.onerror=function(a,b,d,k,c){q!==a&&(a=c instanceof Error?c:Error(a),void 0===d||\"lineNumber\"in a||(a.lineNumber=d),void 0===b||\"fileName\"in a||(a.fileName=b),google.ml(a,!1,void 0,!1,\"SyntaxError\"===a.name||\"SyntaxError\"===a.message.substring(0,11)?2:0));q=null;n&&p>=h&&(window.onerror=null)};})();</script></head><body bgcolor=\"#fff\"><script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){var src=\\'/images/nav_logo229.png\\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}\\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\\n}\\n})();</script><div id=\"mngb\"><div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href=\"http://www.google.com/imghp?hl=en&tab=wi\">Images</a> <a class=gb1 href=\"http://maps.google.com/maps?hl=en&tab=wl\">Maps</a> <a class=gb1 href=\"https://play.google.com/?hl=en&tab=w8\">Play</a> <a class=gb1 href=\"http://www.youtube.com/?gl=US&tab=w1\">YouTube</a> <a class=gb1 href=\"https://news.google.com/?tab=wn\">News</a> <a class=gb1 href=\"https://mail.google.com/mail/?tab=wm\">Gmail</a> <a class=gb1 href=\"https://drive.google.com/?tab=wo\">Drive</a> <a class=gb1 style=\"text-decoration:none\" href=\"https://www.google.com/intl/en/about/products?tab=wh\"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href=\"http://www.google.com/history/optout?hl=en\" class=gb4>Web History</a> | <a  href=\"/preferences?hl=en\" class=gb4>Settings</a> | <a target=_top id=gb_70 href=\"https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.com/&ec=GAZAAQ\" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div></div><center><br clear=\"all\" id=\"lgpd\"><div id=\"lga\"><img alt=\"Google\" height=\"92\" src=\"/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png\" style=\"padding:28px 0 14px\" width=\"272\" id=\"hplogo\"><br><br></div><form action=\"/search\" name=\"f\"><table cellpadding=\"0\" cellspacing=\"0\"><tr valign=\"top\"><td width=\"25%\">&nbsp;</td><td align=\"center\" nowrap=\"\"><input name=\"ie\" value=\"ISO-8859-1\" type=\"hidden\"><input value=\"en\" name=\"hl\" type=\"hidden\"><input name=\"source\" type=\"hidden\" value=\"hp\"><input name=\"biw\" type=\"hidden\"><input name=\"bih\" type=\"hidden\"><div class=\"ds\" style=\"height:32px;margin:4px 0\"><input class=\"lst\" style=\"margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000\" autocomplete=\"off\" value=\"\" title=\"Google Search\" maxlength=\"2048\" name=\"q\" size=\"57\"></div><br style=\"line-height:0\"><span class=\"ds\"><span class=\"lsbb\"><input class=\"lsb\" value=\"Google Search\" name=\"btnG\" type=\"submit\"></span></span><span class=\"ds\"><span class=\"lsbb\"><input class=\"lsb\" id=\"tsuid1\" value=\"I\\'m Feeling Lucky\" name=\"btnI\" type=\"submit\"><script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){var id=\\'tsuid1\\';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}\\nelse top.location=\\'/doodles/\\';};})();</script><input value=\"AHkkrS4AAAAAYkwNZ2K4JBNAOtv0tyIHcUmBtGdQyGZX\" name=\"iflsig\" type=\"hidden\"></span></span></td><td class=\"fl sblc\" align=\"left\" nowrap=\"\" width=\"25%\"><a href=\"/advanced_search?hl=en&amp;authuser=0\">Advanced search</a></td></tr></table><input id=\"gbv\" name=\"gbv\" type=\"hidden\" value=\"1\"><script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){\\nvar a,b=\"1\";if(document&&document.getElementById)if(\"undefined\"!=typeof XMLHttpRequest)b=\"2\";else if(\"undefined\"!=typeof ActiveXObject){var c,d,e=[\"MSXML2.XMLHTTP.6.0\",\"MSXML2.XMLHTTP.3.0\",\"MSXML2.XMLHTTP\",\"Microsoft.XMLHTTP\"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b=\"2\"}catch(h){}}a=b;if(\"2\"==a&&-1==location.search.indexOf(\"&gbv=2\")){var f=google.gbvu,g=document.getElementById(\"gbv\");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id=\"gac_scont\"></div><div style=\"font-size:83%;min-height:3.5em\"><br></div><span id=\"footer\"><div style=\"font-size:10pt\"><div style=\"margin:19px auto;text-align:center\" id=\"WqQANb\"><a href=\"/intl/en/ads/\">Advertising\\xa0Programs</a><a href=\"/services/\">Business Solutions</a><a href=\"/intl/en/about.html\">About Google</a></div></div><p style=\"font-size:8pt;color:#70757a\">&copy; 2022 - <a href=\"/intl/en/policies/privacy/\">Privacy</a> - <a href=\"/intl/en/policies/terms/\">Terms</a></p></span></center><script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){window.google.cdo={height:757,width:1440};(function(){\\nvar a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d=\"CSS1Compat\"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log(\"\",\"\",\"/client_204?&atyp=i&biw=\"+a+\"&bih=\"+b+\"&ei=\"+google.kEI);}).call(this);})();</script> <script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){google.xjs={ck:\\'\\',cs:\\'\\',excm:[]};})();</script>  <script nonce=\"M4OWrIlJlBnl9UwSITdNXw==\">(function(){var u=\\'/xjs/_/js/k\\\\x3dxjs.hp.en_US.DfcTcxDpFPQ.O/am\\\\x3dAOAJAIAEIAE/d\\\\x3d1/ed\\\\x3d1/esmo\\\\x3d1/rs\\\\x3dACT90oF_2ZCH-6H_fdU7aPKP6Nm-IJoFww/m\\\\x3dsb_he,d\\';\\nvar d=this||self,e=function(a){return a};var g;var l=function(a,b){this.g=b===h?a:\"\"};l.prototype.toString=function(){return this.g+\"\"};var h={};\\nfunction n(){var a=u;google.lx=function(){p(a);google.lx=function(){}};google.bx||google.lx()}\\nfunction p(a){google.timers&&google.timers.load&&google.tick&&google.tick(\"load\",\"xjsls\");var b=document;var c=\"SCRIPT\";\"application/xhtml+xml\"===b.contentType&&(c=c.toLowerCase());c=b.createElement(c);if(void 0===g){b=null;var k=d.trustedTypes;if(k&&k.createPolicy){try{b=k.createPolicy(\"goog#html\",{createHTML:e,createScript:e,createScriptURL:e})}catch(q){d.console&&d.console.error(q.message)}g=b}else g=b}a=(b=g)?b.createScriptURL(a):a;a=new l(a,h);c.src=a instanceof l&&a.constructor===l?a.g:\"type_error:TrustedResourceUrl\";var f,m;(f=(a=null==(m=(f=(c.ownerDocument&&c.ownerDocument.defaultView||window).document).querySelector)?void 0:m.call(f,\"script[nonce]\"))?a.nonce||a.getAttribute(\"nonce\")||\"\":\"\")&&c.setAttribute(\"nonce\",f);document.body.appendChild(c);google.psa=!0};google.xjsu=u;setTimeout(function(){n()},0);})();function _DumpException(e){throw e;}\\nfunction _F_installCss(c){}\\n(function(){google.jl={attn:false,blt:\\'none\\',chnk:0,dw:false,dwu:true,emtn:0,end:0,ine:false,injs:\\'none\\',injt:0,lls:\\'default\\',pdt:0,rep:0,snet:true,strt:0,ubm:false,uwp:true};})();(function(){var pmc=\\'{\\\\x22d\\\\x22:{},\\\\x22sb_he\\\\x22:{\\\\x22agen\\\\x22:true,\\\\x22cgen\\\\x22:true,\\\\x22client\\\\x22:\\\\x22heirloom-hp\\\\x22,\\\\x22dh\\\\x22:true,\\\\x22dhqt\\\\x22:true,\\\\x22ds\\\\x22:\\\\x22\\\\x22,\\\\x22ffql\\\\x22:\\\\x22en\\\\x22,\\\\x22fl\\\\x22:true,\\\\x22host\\\\x22:\\\\x22google.com\\\\x22,\\\\x22isbh\\\\x22:28,\\\\x22jsonp\\\\x22:true,\\\\x22msgs\\\\x22:{\\\\x22cibl\\\\x22:\\\\x22Clear Search\\\\x22,\\\\x22dym\\\\x22:\\\\x22Did you mean:\\\\x22,\\\\x22lcky\\\\x22:\\\\x22I\\\\\\\\u0026#39;m Feeling Lucky\\\\x22,\\\\x22lml\\\\x22:\\\\x22Learn more\\\\x22,\\\\x22oskt\\\\x22:\\\\x22Input tools\\\\x22,\\\\x22psrc\\\\x22:\\\\x22This search was removed from your \\\\\\\\u003Ca href\\\\x3d\\\\\\\\\\\\x22/history\\\\\\\\\\\\x22\\\\\\\\u003EWeb History\\\\\\\\u003C/a\\\\\\\\u003E\\\\x22,\\\\x22psrl\\\\x22:\\\\x22Remove\\\\x22,\\\\x22sbit\\\\x22:\\\\x22Search by image\\\\x22,\\\\x22srch\\\\x22:\\\\x22Google Search\\\\x22},\\\\x22ovr\\\\x22:{},\\\\x22pq\\\\x22:\\\\x22\\\\x22,\\\\x22refpd\\\\x22:true,\\\\x22rfs\\\\x22:[],\\\\x22sbas\\\\x22:\\\\x220 3px 8px 0 rgba(0,0,0,0.2),0 0 0 1px rgba(0,0,0,0.08)\\\\x22,\\\\x22sbpl\\\\x22:16,\\\\x22sbpr\\\\x22:16,\\\\x22scd\\\\x22:10,\\\\x22stok\\\\x22:\\\\x22bChmKoBdujCMiay37C1POAfKeEc\\\\x22,\\\\x22uhde\\\\x22:false}}\\';google.pmc=JSON.parse(pmc);})();</script>        </body></html>'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "todos_collec = db.todos"
      ],
      "metadata": {
        "id": "bm4kUilg2X2E"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response = requests.get(\"https://jsonplaceholder.typicode.com/users/1/todos\")"
      ],
      "metadata": {
        "id": "JEgWX5Kc31CZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response.status_code"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uPAct9lU3_wx",
        "outputId": "f578dd04-4032-4673-d56d-4865c5988c2a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "200"
            ]
          },
          "metadata": {},
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response.json()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2cuxRN144H1M",
        "outputId": "d5c69a39-f500-48a3-9d49-460bffbaf06a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'completed': False, 'id': 1, 'title': 'delectus aut autem', 'userId': 1},\n",
              " {'completed': False,\n",
              "  'id': 2,\n",
              "  'title': 'quis ut nam facilis et officia qui',\n",
              "  'userId': 1},\n",
              " {'completed': False, 'id': 3, 'title': 'fugiat veniam minus', 'userId': 1},\n",
              " {'completed': True, 'id': 4, 'title': 'et porro tempora', 'userId': 1},\n",
              " {'completed': False,\n",
              "  'id': 5,\n",
              "  'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum',\n",
              "  'userId': 1},\n",
              " {'completed': False,\n",
              "  'id': 6,\n",
              "  'title': 'qui ullam ratione quibusdam voluptatem quia omnis',\n",
              "  'userId': 1},\n",
              " {'completed': False,\n",
              "  'id': 7,\n",
              "  'title': 'illo expedita consequatur quia in',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 8,\n",
              "  'title': 'quo adipisci enim quam ut ab',\n",
              "  'userId': 1},\n",
              " {'completed': False,\n",
              "  'id': 9,\n",
              "  'title': 'molestiae perspiciatis ipsa',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 10,\n",
              "  'title': 'illo est ratione doloremque quia maiores aut',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 11,\n",
              "  'title': 'vero rerum temporibus dolor',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 12,\n",
              "  'title': 'ipsa repellendus fugit nisi',\n",
              "  'userId': 1},\n",
              " {'completed': False, 'id': 13, 'title': 'et doloremque nulla', 'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 14,\n",
              "  'title': 'repellendus sunt dolores architecto voluptatum',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 15,\n",
              "  'title': 'ab voluptatum amet voluptas',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 16,\n",
              "  'title': 'accusamus eos facilis sint et aut voluptatem',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 17,\n",
              "  'title': 'quo laboriosam deleniti aut qui',\n",
              "  'userId': 1},\n",
              " {'completed': False,\n",
              "  'id': 18,\n",
              "  'title': 'dolorum est consequatur ea mollitia in culpa',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 19,\n",
              "  'title': 'molestiae ipsa aut voluptatibus pariatur dolor nihil',\n",
              "  'userId': 1},\n",
              " {'completed': True,\n",
              "  'id': 20,\n",
              "  'title': 'ullam nobis libero sapiente ad optio sint',\n",
              "  'userId': 1}]"
            ]
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "to_insert = response.json()\n",
        "todos_collec.insert_many(to_insert)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WzjFZ5nr4KAs",
        "outputId": "51ae4151-ec43-4ee0-f4cf-3f91a3a1cf89"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pymongo.results.InsertManyResult at 0x7efffff34cd0>"
            ]
          },
          "metadata": {},
          "execution_count": 60
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor = todos_collec.find({})\n",
        "[item for item in cursor]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pgpKjyLt4mgl",
        "outputId": "c24040be-4609-46c5-f3aa-f3a57c25dc07"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624c019ba836b35c1f13163b'),\n",
              "  'completed': False,\n",
              "  'id': 1,\n",
              "  'title': 'delectus aut autem',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13163c'),\n",
              "  'completed': False,\n",
              "  'id': 2,\n",
              "  'title': 'quis ut nam facilis et officia qui',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13163d'),\n",
              "  'completed': False,\n",
              "  'id': 3,\n",
              "  'title': 'fugiat veniam minus',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13163e'),\n",
              "  'completed': True,\n",
              "  'id': 4,\n",
              "  'title': 'et porro tempora',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13163f'),\n",
              "  'completed': False,\n",
              "  'id': 5,\n",
              "  'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131640'),\n",
              "  'completed': False,\n",
              "  'id': 6,\n",
              "  'title': 'qui ullam ratione quibusdam voluptatem quia omnis',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131641'),\n",
              "  'completed': False,\n",
              "  'id': 7,\n",
              "  'title': 'illo expedita consequatur quia in',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131642'),\n",
              "  'completed': True,\n",
              "  'id': 8,\n",
              "  'title': 'quo adipisci enim quam ut ab',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131643'),\n",
              "  'completed': False,\n",
              "  'id': 9,\n",
              "  'title': 'molestiae perspiciatis ipsa',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131644'),\n",
              "  'completed': True,\n",
              "  'id': 10,\n",
              "  'title': 'illo est ratione doloremque quia maiores aut',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131645'),\n",
              "  'completed': True,\n",
              "  'id': 11,\n",
              "  'title': 'vero rerum temporibus dolor',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131646'),\n",
              "  'completed': True,\n",
              "  'id': 12,\n",
              "  'title': 'ipsa repellendus fugit nisi',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131647'),\n",
              "  'completed': False,\n",
              "  'id': 13,\n",
              "  'title': 'et doloremque nulla',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131648'),\n",
              "  'completed': True,\n",
              "  'id': 14,\n",
              "  'title': 'repellendus sunt dolores architecto voluptatum',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f131649'),\n",
              "  'completed': True,\n",
              "  'id': 15,\n",
              "  'title': 'ab voluptatum amet voluptas',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13164a'),\n",
              "  'completed': True,\n",
              "  'id': 16,\n",
              "  'title': 'accusamus eos facilis sint et aut voluptatem',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13164b'),\n",
              "  'completed': True,\n",
              "  'id': 17,\n",
              "  'title': 'quo laboriosam deleniti aut qui',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13164c'),\n",
              "  'completed': False,\n",
              "  'id': 18,\n",
              "  'title': 'dolorum est consequatur ea mollitia in culpa',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13164d'),\n",
              "  'completed': True,\n",
              "  'id': 19,\n",
              "  'title': 'molestiae ipsa aut voluptatibus pariatur dolor nihil',\n",
              "  'userId': 1},\n",
              " {'_id': ObjectId('624c019ba836b35c1f13164e'),\n",
              "  'completed': True,\n",
              "  'id': 20,\n",
              "  'title': 'ullam nobis libero sapiente ad optio sint',\n",
              "  'userId': 1}]"
            ]
          },
          "metadata": {},
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "### final project\n",
        "#1. comments collection 만들기\n",
        "#2. \"https://jsonplaceholder.typicode.com/posts/1/comments\"\n",
        "#3. 받은 데이터를 밀어넣고 결과 호출"
      ],
      "metadata": {
        "id": "vZ40UkUA4_sJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "comments_collec = db.comments"
      ],
      "metadata": {
        "id": "Fdg1fIiI5Sds"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response = requests.get(\"https://jsonplaceholder.typicode.com/posts/1/comments\")"
      ],
      "metadata": {
        "id": "SGmL_alX5SgQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "response.status_code"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CA4GVptK51cJ",
        "outputId": "3e79b46f-afbb-4263-a9ec-760314d3a9e1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "200"
            ]
          },
          "metadata": {},
          "execution_count": 84
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "to_insert = response.json()"
      ],
      "metadata": {
        "id": "BbRZi8tf53f2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "comments_collec.insert_many(to_insert)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gZ304BhM55rc",
        "outputId": "9d3d5207-8544-46c8-d49d-b924e09f67ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pymongo.results.InsertManyResult at 0x7effffeb4140>"
            ]
          },
          "metadata": {},
          "execution_count": 86
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cursor = comments_collec.find({})\n",
        "[item for item in cursor]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "llzRI64D7ZrQ",
        "outputId": "58c01474-bcdd-43ac-f719-9ce707b1f6f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'_id': ObjectId('624c0395a836b35c1f13164f'),\n",
              "  'body': 'laudantium enim quasi est quidem magnam voluptate ipsam eos\\ntempora quo necessitatibus\\ndolor quam autem quasi\\nreiciendis et nam sapiente accusantium',\n",
              "  'email': 'Eliseo@gardner.biz',\n",
              "  'id': 1,\n",
              "  'name': 'id labore ex et quam laborum',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c0395a836b35c1f131650'),\n",
              "  'body': 'est natus enim nihil est dolore omnis voluptatem numquam\\net omnis occaecati quod ullam at\\nvoluptatem error expedita pariatur\\nnihil sint nostrum voluptatem reiciendis et',\n",
              "  'email': 'Jayne_Kuhic@sydney.com',\n",
              "  'id': 2,\n",
              "  'name': 'quo vero reiciendis velit similique earum',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c0395a836b35c1f131651'),\n",
              "  'body': 'quia molestiae reprehenderit quasi aspernatur\\naut expedita occaecati aliquam eveniet laudantium\\nomnis quibusdam delectus saepe quia accusamus maiores nam est\\ncum et ducimus et vero voluptates excepturi deleniti ratione',\n",
              "  'email': 'Nikita@garfield.biz',\n",
              "  'id': 3,\n",
              "  'name': 'odio adipisci rerum aut animi',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c0395a836b35c1f131652'),\n",
              "  'body': 'non et atque\\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\\nquia voluptas consequuntur itaque dolor\\net qui rerum deleniti ut occaecati',\n",
              "  'email': 'Lew@alysha.tv',\n",
              "  'id': 4,\n",
              "  'name': 'alias odio sit',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c0395a836b35c1f131653'),\n",
              "  'body': 'harum non quasi et ratione\\ntempore iure ex voluptates in ratione\\nharum architecto fugit inventore cupiditate\\nvoluptates magni quo et',\n",
              "  'email': 'Hayden@althea.biz',\n",
              "  'id': 5,\n",
              "  'name': 'vero eaque aliquid doloribus et culpa',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c03f3a836b35c1f131654'),\n",
              "  'body': 'laudantium enim quasi est quidem magnam voluptate ipsam eos\\ntempora quo necessitatibus\\ndolor quam autem quasi\\nreiciendis et nam sapiente accusantium',\n",
              "  'email': 'Eliseo@gardner.biz',\n",
              "  'id': 1,\n",
              "  'name': 'id labore ex et quam laborum',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c03f3a836b35c1f131655'),\n",
              "  'body': 'est natus enim nihil est dolore omnis voluptatem numquam\\net omnis occaecati quod ullam at\\nvoluptatem error expedita pariatur\\nnihil sint nostrum voluptatem reiciendis et',\n",
              "  'email': 'Jayne_Kuhic@sydney.com',\n",
              "  'id': 2,\n",
              "  'name': 'quo vero reiciendis velit similique earum',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c03f3a836b35c1f131656'),\n",
              "  'body': 'quia molestiae reprehenderit quasi aspernatur\\naut expedita occaecati aliquam eveniet laudantium\\nomnis quibusdam delectus saepe quia accusamus maiores nam est\\ncum et ducimus et vero voluptates excepturi deleniti ratione',\n",
              "  'email': 'Nikita@garfield.biz',\n",
              "  'id': 3,\n",
              "  'name': 'odio adipisci rerum aut animi',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c03f3a836b35c1f131657'),\n",
              "  'body': 'non et atque\\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\\nquia voluptas consequuntur itaque dolor\\net qui rerum deleniti ut occaecati',\n",
              "  'email': 'Lew@alysha.tv',\n",
              "  'id': 4,\n",
              "  'name': 'alias odio sit',\n",
              "  'postId': 1},\n",
              " {'_id': ObjectId('624c03f3a836b35c1f131658'),\n",
              "  'body': 'harum non quasi et ratione\\ntempore iure ex voluptates in ratione\\nharum architecto fugit inventore cupiditate\\nvoluptates magni quo et',\n",
              "  'email': 'Hayden@althea.biz',\n",
              "  'id': 5,\n",
              "  'name': 'vero eaque aliquid doloribus et culpa',\n",
              "  'postId': 1}]"
            ]
          },
          "metadata": {},
          "execution_count": 87
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response.text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 72
        },
        "id": "ltzVLa_F7rXn",
        "outputId": "c4d1e516-6685-4ac8-8087-d38329339bca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'[\\n  {\\n    \"postId\": 1,\\n    \"id\": 1,\\n    \"name\": \"id labore ex et quam laborum\",\\n    \"email\": \"Eliseo@gardner.biz\",\\n    \"body\": \"laudantium enim quasi est quidem magnam voluptate ipsam eos\\\\ntempora quo necessitatibus\\\\ndolor quam autem quasi\\\\nreiciendis et nam sapiente accusantium\"\\n  },\\n  {\\n    \"postId\": 1,\\n    \"id\": 2,\\n    \"name\": \"quo vero reiciendis velit similique earum\",\\n    \"email\": \"Jayne_Kuhic@sydney.com\",\\n    \"body\": \"est natus enim nihil est dolore omnis voluptatem numquam\\\\net omnis occaecati quod ullam at\\\\nvoluptatem error expedita pariatur\\\\nnihil sint nostrum voluptatem reiciendis et\"\\n  },\\n  {\\n    \"postId\": 1,\\n    \"id\": 3,\\n    \"name\": \"odio adipisci rerum aut animi\",\\n    \"email\": \"Nikita@garfield.biz\",\\n    \"body\": \"quia molestiae reprehenderit quasi aspernatur\\\\naut expedita occaecati aliquam eveniet laudantium\\\\nomnis quibusdam delectus saepe quia accusamus maiores nam est\\\\ncum et ducimus et vero voluptates excepturi deleniti ratione\"\\n  },\\n  {\\n    \"postId\": 1,\\n    \"id\": 4,\\n    \"name\": \"alias odio sit\",\\n    \"email\": \"Lew@alysha.tv\",\\n    \"body\": \"non et atque\\\\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\\\\nquia voluptas consequuntur itaque dolor\\\\net qui rerum deleniti ut occaecati\"\\n  },\\n  {\\n    \"postId\": 1,\\n    \"id\": 5,\\n    \"name\": \"vero eaque aliquid doloribus et culpa\",\\n    \"email\": \"Hayden@althea.biz\",\\n    \"body\": \"harum non quasi et ratione\\\\ntempore iure ex voluptates in ratione\\\\nharum architecto fugit inventore cupiditate\\\\nvoluptates magni quo et\"\\n  }\\n]'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 88
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##"
      ],
      "metadata": {
        "id": "3iHfE9l48EE6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "https://colab.research.google.com/drive/1bRzpYtf4eDasLYHdRDmM8WW4mY55amZV?usp=sharing#scrollTo=XaGr3mjz4gh0"
      ],
      "metadata": {
        "id": "jjTeBc1c8oZs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "HBqvf3168WJk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}