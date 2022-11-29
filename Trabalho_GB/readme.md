
# Projeto GB - Stickers

Nomes: Kevin Lima e Thiago Monaco
Esse projeto tem como base a exploração da ferramenta OpenCv e Utilização de tecnologias de processamento de imagem.


## Features

- Filtros
    + Sepia
    + Negativo
    + Lapis
    + Verão
    + Inverno
    + Blur
    + GrayScale
    + Sketch
    + Canny
    + Brilho

- Sticker
    - Todos os sticker contidos dentro da pasta `stickers` e configurados no arquivo `stickerConfig.py`
    - Os stickers podem ser alterados pela trackbar `Sticker`

- Captura de tela
    + Captura de tela da imagem ao clicar a tecla `P`

- Aplicação de filtro em imagens contidas dentro da pasta `img` e podem ser alteradas a partir da trackbar `imagem`

- Detecção de Olhos
    + A partir do click da tecla `E` o filtro se ativara ou desativará.
    + Os arquivos utilizados para detecção de olhos são os arquivos 'right.xml' e 'left.xml'

- Detecção de Gestos
    - Ao clicar no letra `G`
    - `Joinha` faça um joinha para a camera
    - `Coração` faça um coração com as mãos para a camera
    - arquivos de configuração `gestureSticker.py`, ``
    - o arquivo para treinamento do modelo deve ser colocado na pasta `model`


## Configuração

Instalar as seguintes dependencias

```bash
python3 pip install pillow
```
```bash
python3 pip install tensorflow
```
```bash
python3 pip install opencv-python
```
```bashy
python3 pip install numpy
```
