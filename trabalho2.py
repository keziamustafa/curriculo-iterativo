import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.header('**Streamlit CV - Cúrriculo Interativo**') 
 

opcoes = ['Boas-vindas', 
		  'Produção Científica', 
		  'Redes Neurais', 
		  'Outras Atividades']

pagina = st.sidebar.selectbox('Navegue pelo menu:', opcoes)
 
###Página inicial

if pagina == 'Boas-vindas':
  st.title('Bem vindos ao meu portifólio')
  st.header('Kezia Alves Mustafa')
  st.text('Brasileira, Solteira, 24 anos')
  st.text('Endereço- Travessa do Meio, 68')
  st.text('Itapuã, Salvador, Bahia')
  st.text('Contato:71986088487, Email:kzia10@hotmail.com')
  st.write("""Currículo lattes: [https://wwws.cnpq.br/cvlattesweb/PKG_MENU.menu?f_cod=91F3D057B07A38B57994E7A54C3DD001# ](https://wwws.cnpq.br/cvlattesweb/PKG_MENU.menu?f_cod=91F3D057B07A38B57994E7A54C3DD001#)""")
  st.header('Objetivo')
  st.text('Desejo construir minha carreira no mercado de trabalho como ciêntista de dados e assim contribuir no desenvolvimento e melhora de diversas empresas ou indústrias que diariamente necessitam tomar decisões')
  st.header('Formação')
  st.text('Cursando bacharelado estatística- UFBA-2015 a 2021')
  st.text('Ensino médio- Marízia Maior- 2011 a 2013')
  st.header('Projetos de pesquisa ')
  st.text('PIBIC 2018-2019- Modelo de regressão em análise de sobrevivência para tempo de natureza discreta')
  st.text('PIBIC 2019/2020- Modelo de regressão com fração de cura em análise de sobrevivência para tempo de natureza discreta')
  st.text('Professora orientadora: Giovana Oliveira Silva')
  st.header('Idiomas')
  st.text('Inglês avançado-CNA(2015 a 2019)')



  st.header('Redes sociais')
  col1, col2 = st.beta_columns(2)
 
  col1.markdown('[![alt text](https://raw.githubusercontent.com/ricardorocha86/StreamlitCV/main/linkedin.png)](https://www.linkedin.com/in/kezia-alves-0709031bb/)')  
  col2.markdown('[![alt text](https://raw.githubusercontent.com/ricardorocha86/StreamlitCV/main/gmail.png)](mailto:keziaamustafa@gmail.com)')

###



elif pagina == 'Produção Científica':
    st.header('Publicação')
    st.write("""
    ### *Artigo publicado em periódico*

    :star: Kézia Alves Mustafa ;Rafael Toledo Costa de Almeida; Paulo Canas Rodrigues\
    **The usefulness of robust multivariate methods: A case study with the menu items of a fast food restaurant chain**. \
    CIÊNCIA NATURA, v.42, p. 17-32, 2020.
    [https://periodicos.ufsm.br/cienciaenatura/article/view/39892/html](https://periodicos.ufsm.br/cienciaenatura/article/view/39892/html).
    
    ### *Iniciação ciêntífica*
    
    :star: Kézia Alves Mustafa ;Giovana Oliveira Silva\
    2018/2019
    **Modelo de regressão usando a distribuição Weibull discreta em análise de sobrevivência.**. \
    [https://drive.google.com/file/d/1E36ft-gYPhVL2XJ1n9IyWQIRk-mB-OxG/view?usp=sharing](https://drive.google.com/file/d/1E36ft-gYPhVL2XJ1n9IyWQIRk-mB-OxG/view?usp=sharing).
    
    :star: Kézia Alves Mustafa ;Giovana Oliveira Silva\
    2019/2020
    **Modelo de regressão com fração de cura usando a distribuição Weibull discreta em análise de sobrevivência.**. \
    [https://drive.google.com/file/d/17T7DFTfwRP_plSbAxUzVDTLQOiefk6pK/view?usp=sharing](https://drive.google.com/file/d/17T7DFTfwRP_plSbAxUzVDTLQOiefk6pK/view?usp=sharing).

    

   
""")


####

elif pagina == 'Redes Neurais':
    st.header('Trabalho da disciplina tópicos A')
    st.write("""
    :star: Kézia Alves Mustafa ;Renan Bispo.\
    **Redes Neurais para a previsão de chuva na cidade de Macaé, localizada no interior do Estado Rio de Janeiro, no período de janeiro de 2016 e janeiro de 2020**. \
    [https://colab.research.google.com/drive/17oJX1ZSbfxUuDPugkSMzTfOd2_u2OXNo?usp=sharing](https://colab.research.google.com/drive/17oJX1ZSbfxUuDPugkSMzTfOd2_u2OXNo?usp=sharing). 
  

""")

############
else:

	st.write("""
    

   
    


    :star: Kézia Alves Mustafa \
    **Análise de agrupamento das pessoas em situação de rua na cidade de Salvador entre março e agosto de 2016**. \
    [https://drive.google.com/file/d/1kEmoa3Rsp5f6-PwxmpBqW-ICSpznq-TV/view?usp=sharing](https://drive.google.com/file/d/1kEmoa3Rsp5f6-PwxmpBqW-ICSpznq-TV/view?usp=sharing).
    O objetivo deste trabalho era verificar a existência de dois grupos que geram uma certa polêmica dentro da população em situação de rua, que são o grupo dos baleiros e não baleiros.
    Existe uma suposição de que o grupo dos baleiros possui melhores condições de vida se comparado ao grupo dos não baleiros. Foi realizada esta análise com o intuito de verificar se existe 
    diferença entre os dois grupos, considerando certas características como a quantidade de drogas consumidas no mês, total de problemas de saúde, entre outros.

    :star: Kézia Alves Mustafa, Caio César Caldas Santos, Rafael Toledo Costa de Almeida.\
    **Classificação dos tipos de vidro utilizando Árvore de Decisão**. \
    [https://drive.google.com/file/d/1cDJbaDTlbSdisNbSY3p9UBdGhBjNiRWh/view?usp=sharing](https://drive.google.com/file/d/1cDJbaDTlbSdisNbSY3p9UBdGhBjNiRWh/view?usp=sharing).
    O vidro é um material que é utilizado para a fabricação de diversos tipos de objetos que são utilizados no dia a dia da população. A sua fabricação é feita com base na utilização de certos elementos químicos,
    tais como o Cálcio, Sódio e Magnésio, por exemplo. Considerando os elementos químicos e o índice de refração do vidro, o método de árvore de decisão foi utilizado com a finalidade de classificar sete tipos de vidro através 
    dessas características.

    




""")
