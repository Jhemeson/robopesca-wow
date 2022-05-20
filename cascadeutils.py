import os


# reads all the files in the /negative folder and generates neg.txt from them.                                 #neg.txt:LER AS FOTOS NEGATIVE E JOGA PRO neg.txt
# we'll run it manually like this:
# $ python
# Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from cascadeutils import generate_negative_description_file
# >>> generate_negative_description_file()
# >>> exit()
def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')

# the opencv_annotation executable can be found in opencv/build/x64/vc15/bin                                                            #pos.txt:
# generate positive description file using:
# $ D:/Programação/Programas/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive

# You click once to set the upper left corner, then again to set the lower right corner.
# Press 'c' to confirm.
# Or 'd' to undo the previous confirmation.
# When done, click 'n' to move to the next image.
# Press 'esc' to exit.
# Will exit automatically when you've annotated all of the images

# generate positive samples from the annotations to get a vector file using:
# $ D:/Programação/Programas/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec                     #pos.vec
#-num 1000 é o número de retângulos       LEMBRAR DE  TROCAR "\"" POR "/"" LÁ NO POS.
#"vec-file has to contain >= (numPose + (numStages-1) * (1 - minHitRate) * numPose) + S".  Referência para saber quantidade de sample pra colocar no excel

#####train the cascade classifier model using:####### dentro da pasta que tiver seu main
# $ D:/Programação/Programas/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 70 -numNeg 600 -numStages 12 -w 24 -h 24
#numPos e numNeg são as quantidades de exemplos utilizados pra treinar. Número de numPos precisa ser menos ou igual do que a quantidade de imagens positives printadas desenhados. NumNeg deve ser metade do NumPos ou o dobro do NumPos ou quanto mais melhor (precisa testar um desses dois). -numStages 10 são quantos estágios de treino levará. Aumente o estágio se ainda aparecer muitos retangulos na tela.
#se usar um terminal fora do VScode para treinar, deixará o vscode livre pra usar. Lembrar de excluir os arquivos cascade xml, mas antes precisa salvar o modelo já treinado, salvando o 'cascade.xml' em algum outro lugar. Se tiver muito falso alarme no treino, o melhor é printar mais negative photos ou treinar mais estagios.

# HR=hit rate, FA=false alarm, N=weak layer number, 1 e 2 são camadas mais externas, 4 ou ultima da tabela são camadas mais baixas (ultimas camadas é o que queremos que da menos false alarm). Se no AcceptanceRatio tiver com mais de 4 zeros, então já treino suficiente


# my final classifier training arguments:
# $ D:/Programação/Programas/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 2000 -precalcIdxBufSize 2000 -numPos 74 -numNeg 900 -numStages 10 -w 24 -h 24 -maxFalseAlarmRate 0.1 -minHitRate 0.999
