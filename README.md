# data-fusion-contest
Решение первой задачи контеста https://boosters.pro/championship/data_fusion/overview  
Скор на публичном лидерборде 0.8562009 (19 место из 265).  
Скор на приватном лидерборде 0.8538438 (18 место из 265).  
Основная идея решения:
1. Дообучаем distilbert на задаче masked language modeling. 
2. Модель из п.1. дообучаем на задаче многоклассовой классификации. Используем только размеченные данные.
3. Используем агломеративную кластеризацию для псевдо разметки (подробнее про метод можно прочитать здесь https://www.aclweb.org/anthology/2020.coling-main.438.pdf).  
Псевдо размеченные данные расположены в data/pseudo.csv.
5. Используем SVM + TFIDF на размеченных и псевдо размеченных данных.

Notebooks:
1. data_fusion_task1_BERTML.ipynb - дообучение distilbert на задаче masked language modeling.
2. DISTILBERT_with_pseudo.ipynb - дообучение distilbert из п.1 на задаче классификации item_name из чеков и псевдо разметка данных.
3. task1_data_fusion.ipynb - SVM + TFIDF классификация item_name из чеков.

Примечания:
1. Нужно добавить файл с исходными данными data_fusion_train.parquet в папку data.
2. Если нет возможности дообучить модели, то нужно загрузить модель, которая получилась в результате выполнения DISTILBERT_with_pseudo.ipynb, и поместить её в папку distilbert_uncased_for_pseudolab. Ссылка на модель https://drive.google.com/file/d/1ghx1gSb6n3JvxvpN-0qbcxOIajwzjX7I/view?usp=sharing
