{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "180~191",
      "provenance": [],
      "authorship_tag": "ABX9TyMTlA88SFs2ku1DvtvDfO7M"
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qanz9x-R8itR",
        "outputId": "08023928-d322-45bd-c9ad-c4a9c24d1bf7"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['101호', '102호'], ['201호', '202호'], ['301호', '302호']]"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ],
      "source": [
        "#181: 하나의 행을 하나의 리스트로 총 3개의 리스트 이차원 apart 정의\n",
        "\n",
        "apart = [['101호','102호'],['201호','202호'],['301호','302호']]\n",
        "apart "
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#182\n",
        "stock = [['시가','100','200','300'],['종가','80','210','330']]\n",
        "stock"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7NLvZeOe94WJ",
        "outputId": "ca374a8f-ec99-4c97-8b0b-442858c63946"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['시가', '100', '200', '300'], ['종가', '80', '210', '330']]"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#183 딕셔너리 체크\n",
        "stock = {'시가':['100','200','300'], '종가':['80','210','330']}\n",
        "stock"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "whe__8Vj-a0j",
        "outputId": "67087812-a152-4159-e17c-b543e3bd0e06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'시가': ['100', '200', '300'], '종가': ['80', '210', '330']}"
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
        "#184\n",
        "\n",
        "stock = {'10/10':['80','110','70','90'],'10/11':['210','230','190','200']}\n",
        "stock"
      ],
      "metadata": {
        "id": "iEAy_c_J_D_u",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bb53292e-12cf-48f6-960c-167e277962e4"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'10/10': ['80', '110', '70', '90'], '10/11': ['210', '230', '190', '200']}"
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
        "#185\n",
        "apart = [ [101, 102], [201, 202], [301, 302] ]\n",
        "\n",
        "for row in apart:\n",
        "    for col in row:\n",
        "        print(col, \"호\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FvF9DOaNItud",
        "outputId": "7f6b644c-6dee-4cec-e4c3-e62b49a17913"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "101 호\n",
            "102 호\n",
            "201 호\n",
            "202 호\n",
            "301 호\n",
            "302 호\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#186\n",
        "apart = [ [101, 102], [201, 202], [301, 302] ]\n",
        "\n",
        "for row in apart[::-1]:\n",
        "    for col in row:\n",
        "        print(col, '호')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WUg00ZMxI03h",
        "outputId": "078bc99b-0b07-4e0d-9395-e09ed04c17c9"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "301 호\n",
            "302 호\n",
            "201 호\n",
            "202 호\n",
            "101 호\n",
            "102 호\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#187\n",
        "apart = [ [101, 102], [201, 202], [301, 302] ]\n",
        "\n",
        "for row in apart[::-1]:\n",
        "    for col in row[::-1]:\n",
        "        print(col,'호')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k640dZIYJPrH",
        "outputId": "4f1f1c01-9911-481a-b1e7-a688046a0a9b"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "302 호\n",
            "301 호\n",
            "202 호\n",
            "201 호\n",
            "102 호\n",
            "101 호\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##188\n",
        "\n",
        "apart = [ [101, 102], [201, 202], [301, 302] ]\n",
        "\n",
        "for row in apart:\n",
        "    for col in row:\n",
        "        print(col, \"호\")\n",
        "        print(\"-\" * 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "myxTxAzRJkOi",
        "outputId": "b97851e0-e9a2-42cc-958c-5dcb1cfd3dc6"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "101 호\n",
            "-----\n",
            "102 호\n",
            "-----\n",
            "201 호\n",
            "-----\n",
            "202 호\n",
            "-----\n",
            "301 호\n",
            "-----\n",
            "302 호\n",
            "-----\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#189\n",
        "apart = [ [101, 102], [201, 202], [301, 302] ]\n",
        "\n",
        "for row in apart:\n",
        "    for col in row:\n",
        "        print(col, \"호\")\n",
        "    print(\"-\" * 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X6wFx6rLKDX-",
        "outputId": "44267687-f32d-4630-de07-a79d322d6f4a"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "101 호\n",
            "102 호\n",
            "-----\n",
            "201 호\n",
            "202 호\n",
            "-----\n",
            "301 호\n",
            "302 호\n",
            "-----\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#190\n",
        "\n",
        "apart = [ [101, 102], [201, 202], [301, 302] ]\n",
        "\n",
        "for row in apart:\n",
        "    for col in row:\n",
        "        print(col, \"호\")\n",
        "print(\"-\" * 5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZgW_tS-IQqha",
        "outputId": "ed424ef1-9314-4592-eaac-f077e795de01"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "101 호\n",
            "102 호\n",
            "201 호\n",
            "202 호\n",
            "301 호\n",
            "302 호\n",
            "-----\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "OgZSaEjKQzZr"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}