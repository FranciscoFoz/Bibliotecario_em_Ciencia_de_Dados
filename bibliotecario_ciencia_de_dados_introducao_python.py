{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Bibliotecario_Ciencia_de_Dados_Introducao_Python.ipynb",
      "provenance": []
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
      "cell_type": "markdown",
      "metadata": {
        "id": "23XiGBEgmmzT"
      },
      "source": [
        "Autor: [Francisco Foz](https://www.linkedin.com/in/francisco-tadeu-foz/)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "loFuAcfIkYgm"
      },
      "source": [
        "# <font color = green> INTRODUÇÃO AO PYTHON\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "n0Fth3Lpkq5E"
      },
      "source": [
        "Este notebook faz parte de um projeto iniciado por mim, Francisco Foz, integrante do time Alura Stars. Com o objetivo de auxiliar na disseminação da informação em Ciência de Dados para a área da biblioteconomia. Utilizando do livro \"Data Science do zero\" de Joel Grus.\n",
        "Abordarei alguns conceitos básicos da linguagem para ilustrar e adentrar na ferramenta.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xdFVjwpFd1Xf"
      },
      "source": [
        "#Variaveis"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mk-Zv6kaeemN"
      },
      "source": [
        "mes = 11"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "9iJNnNFad4je",
        "outputId": "d958649d-7e0a-4a77-fc39-8a505a5df2ae"
      },
      "source": [
        "autor = \"Le Coadic, Yves-François\"\n",
        "autor"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Le Coadic, Yves-François'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iI1pGw0bhxgV"
      },
      "source": [
        "subject =\t\"Biblioteconomia\"         #string\n",
        "\n",
        "subject_2 = \"Ciência da informação\" #string\n",
        "\n",
        "date\t= 2004                        #int\n",
        "\n",
        "price = 44.90                       #float\n",
        "\n",
        "comparativo = subject == subject_2   #bool\n",
        "\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NHy2obYuW6Ts"
      },
      "source": [
        "## Identação\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F0-GeB1-Z4Jd",
        "outputId": "2f560e71-3b22-4f47-f992-aa67edbecace"
      },
      "source": [
        "def saudacao_inicial():\n",
        "  print('Olá usuário! O que você gosta de ler?')\n",
        "saudacao_inicial()\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Olá usuário! O que você gosta de ler?\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1D-KlkYLnwW2"
      },
      "source": [
        "#Funções"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3AsCCqj2kfDm",
        "outputId": "91d7b08c-f4fc-4fc3-cb51-87f699084417"
      },
      "source": [
        "def saudacao_inicial():\n",
        "  nome = input('Qual é o seu nome?')\n",
        "  print(f'Olá {nome}! O que você gosta de ler?')\n",
        "saudacao_inicial()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Qual é o seu nome?FOZ\n",
            "Olá FOZ! O que você gosta de ler?\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KYNb934Dp0r3"
      },
      "source": [
        "#Listas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IPKX5YH8npAR",
        "outputId": "c2935f6c-f1db-4033-85c6-c62bd20eae38"
      },
      "source": [
        "assuntos = ['Amazônia - História',\t\n",
        "            'Gestão ambiental', \n",
        "            'Sistemas de informação geográfica', \n",
        "            'Amazon', \n",
        "            'Environmental management']\n",
        "assuntos"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Amazônia - História',\n",
              " 'Gestão ambiental',\n",
              " 'Sistemas de informação geográfica',\n",
              " 'Amazon',\n",
              " 'Environmental management']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WWD21VNYqp5b",
        "outputId": "a6fa850c-437c-4da1-ed2e-c8a31e1fa3be"
      },
      "source": [
        "print(assuntos [0])\n",
        "print(assuntos [1])\n",
        "print(assuntos [2])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Amazônia - História\n",
            "Gestão ambiental\n",
            "Sistemas de informação geográfica\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZhW56q27sQSR",
        "outputId": "0c53658e-6d32-4123-aaa4-5fd6ea24b328"
      },
      "source": [
        "assuntos [2:4]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Sistemas de informação geográfica', 'Amazon']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9iHZF4ifrR3y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a9dd84d5-7df9-40c5-b0de-898a2787af30"
      },
      "source": [
        "assuntos.append('Geographic information system')\n",
        "assuntos"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Amazônia - História',\n",
              " 'Gestão ambiental',\n",
              " 'Sistemas de informação geográfica',\n",
              " 'Amazon',\n",
              " 'Environmental management',\n",
              " 'Geographic information system']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nW2RivBND5ow"
      },
      "source": [
        "#Tuplas\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2gPIgzyzD7Hx"
      },
      "source": [
        "dias_da_Semana = (\"Dom\",\"Seg\",\"Ter\",\"Qua\",\"Qui\",\"Sex\",\"Sab\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "wrBWS4oeEMkh",
        "outputId": "f350290f-823b-45d9-9ba1-d786fc30d978"
      },
      "source": [
        "dias_da_Semana[0]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Dom'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "79MweaM4Q4-R"
      },
      "source": [
        "#Dicionários"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qp4sO4TvQ6pz"
      },
      "source": [
        "db_livro = {\n",
        "  \"title\" :\t\"A ciência da informação\",\n",
        "  \"creator\"\t: \"Le Coadic, Yves-François\",\n",
        "  \"subject\" :\t[\"Biblioteconomia\",\t\"Ciência da informação\"],\n",
        "  \"description\"\t: \"Tradução de: La science de l'information\",\n",
        "  \"publisher\" :\t\"Briquet de Lemos\",\n",
        "  \"date\" :\t\"2004\",\n",
        "  \"type\" :\t\"LIVRO\",\n",
        "  \"format\" :\t\"124p. : il.\",\n",
        "  \"identifier\" :\t[\"8585637234 (broch.)\"],\n",
        "  \"language\" :\t[\t\"por\", \"fre\"]\n",
        "  }"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Zvh96KfLR4R5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "c4d319cf-c9df-4e81-f1a3-8a44f37f2613"
      },
      "source": [
        "db_livro[\"creator\"]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Le Coadic, Yves-François'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kVy9qGhWUAal",
        "outputId": "5da85d48-2e50-419b-c526-bee4b562edc6"
      },
      "source": [
        "db_livro[\"subject\"]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Biblioteconomia', 'Ciência da informação']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "ZQugEZIBUYu9",
        "outputId": "46a35840-cd8b-4980-ecb6-0c1966ca57e4"
      },
      "source": [
        "db_livro[\"subject\"][0]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Biblioteconomia'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Adbo1sz8_mpA"
      },
      "source": [
        "#Condicionais"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5eL-dZno_okY",
        "outputId": "80838f09-a525-4038-dd26-7e1054af15e6"
      },
      "source": [
        "qtd_usuarios = int(input('Qual é a quantidade de usuarios da biblioteca? '))\n",
        "\n",
        "if qtd_usuarios <= 50:\n",
        "  print('A biblioteca tem poucos usuarios')\n",
        "elif qtd_usuarios <= 200:\n",
        "  print('A biblioteca tem uma quantidade razoável de usuarios')\n",
        "elif qtd_usuarios <= 500:\n",
        "  print('A biblioteca tem muitos usuarios')\n",
        "else:\n",
        "  print('A biblioteca tem um número muito grande de usuarios')\n",
        "  "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Qual é a quantidade de usuarios da biblioteca? 1000\n",
            "A biblioteca tem um número muito grande de usuarios\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wvBa7DZlfPRa"
      },
      "source": [
        "#Repetição"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vNIpro-yXqGM"
      },
      "source": [
        "autores = [\n",
        "  \"Dante Alighieri\",\n",
        "  \"Machado de Assis\",\n",
        "  \"Franz Kafka\",\n",
        "  \"Luís Vaz de Camões\",\n",
        "  \"William Shakespeare\",\n",
        "  \"José Saramago\",\n",
        "  \"Aristóteles\",\n",
        "  \"Júlio Verne\",\n",
        "  \"Fernando Pessoa\",\n",
        "  \"José de Alencar\",\n",
        "  \"Euclides da Cunha\",\n",
        "  \"Thomas Morus\"\n",
        "]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cGi0_gHsfRJZ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "77e353d1-5270-4e40-f9f3-31d64e5a9c3c"
      },
      "source": [
        "for autor in autores:\n",
        "  print(autor)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Dante Alighieri\n",
            "Machado de Assis\n",
            "Franz Kafka\n",
            "Luís Vaz de Camões\n",
            "William Shakespeare\n",
            "José Saramago\n",
            "Aristóteles\n",
            "Júlio Verne\n",
            "Fernando Pessoa\n",
            "José de Alencar\n",
            "Euclides da Cunha\n",
            "Thomas Morus\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MHbJD3_WkJ-E"
      },
      "source": [
        "numero = -10\n",
        "while (numero < 10):\n",
        "  numero += 1\n",
        "  print(numero)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jeG39GFjIUAX"
      },
      "source": [
        "#Veracidade"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cYq3Gg7TIWmQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "114469a4-0f32-4ca3-b54e-a5a9a03ac964"
      },
      "source": [
        "10 < 5"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z307StcFcKxh",
        "outputId": "6547d76e-fdb8-4f0b-ae2b-dd98f8d337c2"
      },
      "source": [
        "20 > 10"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EswCugh3fo2C"
      },
      "source": [
        "False   #falso\n",
        "None    #nulo\n",
        "0       #zero\n",
        "''      #string vazia\n",
        "[]      #lista vazia\n",
        "()      #tupla vazia\n",
        "{}      #dicionário vazio"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bo-N5w-SkSYD",
        "outputId": "005ac2a2-e340-485c-d6e7-f2c0347bdbba"
      },
      "source": [
        "lista_all = [5, True, (2,2)]\n",
        "all(lista_all)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SHc90wZFlp-Q",
        "outputId": "63b0ea34-a81f-474a-9fbc-ef61fe545c52"
      },
      "source": [
        "lista_all = [5, True, ()]\n",
        "all(lista_all)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HLlsuDwVmSp3",
        "outputId": "8673779d-c8d1-4480-d357-478a49e804f2"
      },
      "source": [
        "lista_any = [1, 0, ()]\n",
        "any(lista_any)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dHLJLcZ9mahO",
        "outputId": "65769c5b-2b66-4dcd-a775-9ebcd61e4699"
      },
      "source": [
        "lista_any = [0, 0, ()]\n",
        "any(lista_any)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2GdlCGoWvulZ"
      },
      "source": [
        "#Importar Módulos\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NAqVVPrNv1dw"
      },
      "source": [
        "import collections "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TAqyYUT4x4xC",
        "outputId": "6fa36034-9dbb-4249-fee6-b3714b48c7f0"
      },
      "source": [
        "import collections as coll\n",
        "coll.Counter"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "collections.Counter"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nDdRVVuGzHc5",
        "outputId": "52ffc027-ed33-46f9-9d7e-ffe72094f834"
      },
      "source": [
        "import pandas as pd\n",
        "pd"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<module 'pandas' from '/usr/local/lib/python3.7/dist-packages/pandas/__init__.py'>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c5Ja6UEix6-r",
        "outputId": "96bbe955-5ee6-4e3b-93f8-7fea7acaefbc"
      },
      "source": [
        "from collections import Counter \n",
        "Counter"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "collections.Counter"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CRj8xzUlXXP_"
      },
      "source": [
        "#Contador"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PM2lhQ_SYBbG"
      },
      "source": [
        "interesses = [\n",
        "  'biblioteconomia',\n",
        "  'gatos',\n",
        "  'livros',\n",
        "  'ciencia de dados',\n",
        "  'filmes',\n",
        "  'gatos',\n",
        "  'livros',\n",
        "  'séries',\n",
        "  'biblioteconomia',\n",
        "  'filmes',\n",
        "  'séries',\n",
        "  'gatos',\n",
        "  'trekking',\n",
        "  'leitura',\n",
        "  'história',\n",
        "  'matemática',\n",
        "  'filmes',\n",
        "  'séries',\n",
        "  'livros',\n",
        "  'ciencia de dados',\n",
        "  'livros',\n",
        "  'filmes',\n",
        "  'biblioteconomia'\n",
        "  ]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3TxeTUNqYONm",
        "outputId": "500993b2-3957-4c5c-88f3-5efefde55457"
      },
      "source": [
        "contagem_interesse = Counter(interesses)\n",
        "contagem_interesse"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Counter({'biblioteconomia': 3,\n",
              "         'ciencia de dados': 2,\n",
              "         'filmes': 4,\n",
              "         'gatos': 3,\n",
              "         'história': 1,\n",
              "         'leitura': 1,\n",
              "         'livros': 4,\n",
              "         'matemática': 1,\n",
              "         'séries': 3,\n",
              "         'trekking': 1})"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ml6qDHHscvq-",
        "outputId": "963e6513-6bc1-4a1c-8040-398d8f572562"
      },
      "source": [
        "for interesse, count in contagem_interesse.most_common(2):\n",
        "    print (interesse, count)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "livros 4\n",
            "filmes 4\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "plRDpXp_5xbE"
      },
      "source": [
        "#Conjunto"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9aQeCAY05zV1",
        "outputId": "207b05d6-e815-49b6-cba0-f085ad32bd42"
      },
      "source": [
        "id_contratos = set()\n",
        "id_contratos.add(1)\n",
        "id_contratos.add(2)\n",
        "id_contratos.add(3)\n",
        "id_contratos.add(4)\n",
        "id_contratos.add(5)\n",
        "id_contratos\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{1, 2, 3, 4, 5}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QKjYWb9T7UWa"
      },
      "source": [
        "id = 12\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tJroKebK7WTC",
        "outputId": "6e1116cf-4260-4025-87e6-f9108871dbde"
      },
      "source": [
        "id in id_contratos\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HkmHzyKumqvc"
      },
      "source": [
        "#Ordenação"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "h_1KdR3Pmvl8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2072ceb5-0fd7-4f73-9654-874218bf317c"
      },
      "source": [
        "ordenacao = [10,2,8,4,6,0]\n",
        "print(sorted(ordenacao))    #sorted não altera a lista\n",
        "print(ordenacao)            \n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0, 2, 4, 6, 8, 10]\n",
            "[10, 2, 8, 4, 6, 0]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3f579D6hEnCl",
        "outputId": "30d717ad-7b2c-4712-ae85-9ff4458a89dd"
      },
      "source": [
        "ordenacao.sort()            #.sort altera a lista\n",
        "print(ordenacao)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0, 2, 4, 6, 8, 10]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l7CNldODEsoT",
        "outputId": "76717fbe-760d-4b54-df62-a586d2a8d315"
      },
      "source": [
        "ordenacao"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0, 2, 4, 6, 8, 10]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k53k7Ma7FWak",
        "outputId": "1a34fa55-47d4-4889-b048-79c90a8ebac8"
      },
      "source": [
        "qualis = ['B1','A1','B4']\n",
        "\n",
        "sorted(qualis, reverse=True)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['B4', 'B1', 'A1']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9aBL18L0MJAw"
      },
      "source": [
        "#Aleatoriedade"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IyI6L4iKG3Aj"
      },
      "source": [
        "import random"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OvcxF9LEMNS0",
        "outputId": "80752a26-6ff5-4421-b9c3-34cf03482e84"
      },
      "source": [
        "random.random()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.43363336680510567"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-vXMA1g9MREk",
        "outputId": "6ae3641f-b205-4a7a-c5d1-164527b2b84e"
      },
      "source": [
        "random.random()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.5317198217606026"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DNKmQcrBMSVs",
        "outputId": "e3de2d54-7245-4aef-d082-1de2395eda24"
      },
      "source": [
        "random.seed(10)\n",
        "print(random.random())\n",
        "random.seed(2)\n",
        "print(random.random())\n",
        "random.seed(10)\n",
        "print(random.random())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.5714025946899135\n",
            "0.9560342718892494\n",
            "0.5714025946899135\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n_ssC38MN1kj",
        "outputId": "b7e0c3f2-2fcc-4ca2-f300-ff2220acbcd4"
      },
      "source": [
        "random.random()\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9424502837770503"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bZEAVd62OBAw",
        "outputId": "2e11d420-3958-4d26-a942-4e6198d342a0"
      },
      "source": [
        "random.randrange(10)    #será um número entre 0 e 10"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QOdBILv-Oo8Y",
        "outputId": "9a81a5d9-63d0-48b3-ce8b-f61e99cc5941"
      },
      "source": [
        "random.randrange(10,100) #será um número entre 10 e 100"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "83"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 84
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "QLBVPUBcPIAG",
        "outputId": "5467f6fb-6bdf-4620-a771-c54de481178d"
      },
      "source": [
        "periodicos = [\n",
        "              'BRITISH JOURNAL OF NURSING', \n",
        "              'CIRCULATION (NEW YORK, N.Y.)', \n",
        "              'EUROPEAN JOURNAL OF HEART FAILURE', \n",
        "              'EUROPEAN JOURNAL OF ENDOCRINOLOGY'\n",
        "              ]\n",
        "random.choice(periodicos)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'CIRCULATION (NEW YORK, N.Y.)'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 93
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z1bMGZl6Q2dk",
        "outputId": "a9c71460-5690-4453-b67a-c080e9d4c888"
      },
      "source": [
        "lista_de_numeros = range(100)\n",
        "amostra = random.sample(lista_de_numeros,4)   #escolherá 4 números dentre a lista de 0 a 100 passada\n",
        "amostra"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[17, 58, 98, 30]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 102
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YW7FVDrmUu7-"
      },
      "source": [
        "#Expressões Regulares"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wunpmo87Uwoy"
      },
      "source": [
        "import re       #módulo de expressões regulares\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xP-A3Sc78S-_"
      },
      "source": [
        "#Compreensões de Listas\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fNOKFbDb8WAG"
      },
      "source": [
        "lista = range(5)\n",
        "\n",
        "for x in lista:         \n",
        "  if x % 2 == 0:    \n",
        "    print(x)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q6XzfsLMIy44",
        "outputId": "e9020f39-6825-4879-acd6-0c569f5f1af4"
      },
      "source": [
        "numeros_pares = [x for x in lista if x % 2 == 0]\n",
        "numeros_pares"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0, 2, 4]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y9Uq6jrEKAlU",
        "outputId": "e06800f4-ad42-42d6-8dc7-10086d090e5e"
      },
      "source": [
        "range(0,5)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "range(0, 5)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VgU73agEPDkN"
      },
      "source": [
        "#Geradores e Iteradores"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jCrxHZaYX0e8"
      },
      "source": [
        "def exemplo_de_gerador():\n",
        "  x = 0\n",
        "  while x < 1000000: \n",
        "    print(x)\n",
        "    x = x + 1\n",
        "exemplo_de_gerador()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J5iKNceaS-2C",
        "outputId": "7debe421-de41-457f-f3aa-201ba31147aa"
      },
      "source": [
        "def exemplo_de_gerador():\n",
        "  x = 0\n",
        "  while x < 1000000: \n",
        "    print(x)\n",
        "    yield x\n",
        "    x = x + 1\n",
        "exemplo_de_gerador()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<generator object exemplo_de_gerador at 0x7f6d11cde0d0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lNdpG0SAUeaI",
        "outputId": "4cf7ce56-a6c1-460b-eccb-ef86f6975f42"
      },
      "source": [
        "gerador = exemplo_de_gerador()\n",
        "next(gerador)\n",
        "next(gerador)\n",
        "next(gerador)\n",
        "next(gerador)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 93
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eNVnkktjYfBY"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ySkb28X1eLIC"
      },
      "source": [
        "#Programação Orientada a Objeto"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R7ftdEq3eOUG",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "outputId": "239b8cd5-c81f-47c3-98a6-4afb0c1b21c1"
      },
      "source": [
        "class UsuarioUniversitario:\n",
        "  def __init__(self, id, curso):\n",
        "    self.__id = id;\n",
        "    self.__curso = curso;\n",
        "    self.__disciplinas_ativas = disciplinas_ativas\n",
        "\n",
        "  def consulta(self):\n",
        "    # Codigo para consultar informação\n",
        "    \n",
        "  def pega_emprestado(self):\n",
        "    # Codigo para pegar emprestado um recurso informacional\n",
        "\n",
        "  def devolve(self):\n",
        "    # Codigo para devolver recurso informacional\n",
        "\n",
        "  def solicita_referencia(self):\n",
        "    # Codigo para solicitar referência ao bibliotecário"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-17-3ca90638503a>\"\u001b[0;36m, line \u001b[0;32m10\u001b[0m\n\u001b[0;31m    def pega_emprestado(self):\u001b[0m\n\u001b[0m      ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Jq8DqI5zR0gO"
      },
      "source": [
        "#Ferramentas Funcionais\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cIuopMYgR5tg",
        "outputId": "46acfd2d-f801-4019-f6ea-f2ae28c0c9bb"
      },
      "source": [
        "def subtrair_1(x):\n",
        "  return x - 1\n",
        "\n",
        "numeros_pares = [2,4,6,8,10]\n",
        "\n",
        "numeros_impares = map(subtrair_1, numeros_pares)\n",
        "print(list(numeros_impares))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 3, 5, 7, 9]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PS1UMw8NtjO6"
      },
      "source": [
        "from functools import reduce"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zwDlClq9qtvZ",
        "outputId": "4ecd0524-8b97-4a03-d630-866be0527fb7"
      },
      "source": [
        "def multiplicar(x, y):\n",
        "  return x * y\n",
        "\n",
        "numeros_multiplicados = reduce(multiplicar, numeros_pares)\n",
        "numeros_multiplicados"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3840"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WIor7jsjwQZF",
        "outputId": "f2e4fd9f-f6be-46fa-97d1-c838d2025da6"
      },
      "source": [
        "def numeros_negativos(x):\n",
        "  if x < 0: \n",
        "    return x\n",
        "\n",
        "lista_numeros = range(-10,100)\n",
        "print(list(filter(numeros_negativos, lista_numeros)))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5OG7rQ0e51OL"
      },
      "source": [
        "#Enumeração"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3ZrkEJ9252kT",
        "outputId": "f5ea285e-2b8c-423e-d456-b014527643c8"
      },
      "source": [
        "CDD = ['Generalidades', \n",
        "       'Filosofia',\n",
        "       'Religião',\n",
        "       'Ciências sociais',\n",
        "       'Línguas',\n",
        "       'Ciências puras',\n",
        "       'Ciências aplicadas',\n",
        "       'Artes',\n",
        "       'Literatura',\n",
        "       'História e geografia']\n",
        "\n",
        "print(list(enumerate(CDD)))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[(0, 'Generalidades'), (1, 'Filosofia'), (2, 'Religião'), (3, 'Ciências sociais'), (4, 'Línguas'), (5, 'Ciências puras'), (6, 'Ciências aplicadas'), (7, 'Artes'), (8, 'Literatura'), (9, 'História e geografia')]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_eHJoICy6kAr"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0Mrd37blbcIj"
      },
      "source": [
        "#Descompactação de Zip e argumentos\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cer5jVsqbfQ8",
        "outputId": "fa4c93be-073c-4b5f-d506-1b74e333c75d"
      },
      "source": [
        "lista_alfabetica = ['a','b','c']\n",
        "lista_numerica =    [1,2,3]\n",
        "lista_alfanumerica = list(zip(lista_alfabetica,lista_numerica))\n",
        "lista_alfanumerica"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('a', 1), ('b', 2), ('c', 3)]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9r0Hd4r-oGzf",
        "outputId": "fb7ed935-2b9a-422a-fac4-e7fc5835e88b"
      },
      "source": [
        "letras, numeros = (zip(*lista_alfanumerica))\n",
        "letras, numeros"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(('a', 'b', 'c'), (1, 2, 3))"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yTdOKREk2acY"
      },
      "source": [
        "#Args e Kwargs\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yNpRq73j2cy8"
      },
      "source": [
        "def assuntos_livro(titulo, *args):\n",
        "    print('Título: ', titulo)\n",
        "    for assunto in args:\n",
        "        print('Assunto: ', assunto)\n"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1cJ_zUqX67l7",
        "outputId": "3406e0ed-29d7-429e-bee1-7aedb0d4038c"
      },
      "source": [
        "assuntos_livro('A aventura do livro', \n",
        "               'Livros e leitura - História',\n",
        "               'Comunicação escrita', \n",
        "               'Tecnologia da informação - Aspectos sociais')\n"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Título:  A aventura do livro\n",
            "Assunto:  Livros e leitura - História\n",
            "Assunto:  Comunicação escrita\n",
            "Assunto:  Tecnologia da informação - Aspectos sociais\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kNmu-mrn83yQ",
        "outputId": "ab7f0d8c-1e23-4712-fef2-1aebf1c36b9b"
      },
      "source": [
        "assuntos_livro('Crime e Castigo', 'Ficção Russa')"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Título:  Crime e Castigo\n",
            "Assunto:  Ficção Russa\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gt1BGWf6Ra4G",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d214e788-a0d4-4a67-f4da-676d40109087"
      },
      "source": [
        "def autor_do_livro(titulo,**kwargs):\n",
        "      autor = kwargs.get('creator')\n",
        "      print(autor)\n",
        "\n",
        "autor_do_livro('O Pensamento do exterior', \n",
        "               creator='Foucalt, Michel, 1926-1984', subject='Filosofia Francesa')"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Foucalt, Michel, 1926-1984\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
