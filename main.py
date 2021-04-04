def date_sorter():
        
    import re
    from datetime import date

    answer = df.copy()
    answer[:] = df.apply(lambda x: re.findall(r"(\d{1,2})[/-](\d{1,2})[/-]([12][09]\d{2})",x))
    answer[:] += df.apply(lambda x: re.findall(r"(\d{1,2})[/-](\d{1,2})[/-](\d{2})",x))
    answer[:] += df.apply(lambda x: re.findall(r"(\d{1,2})[/-]([12][09]\d{2})",x))
    answer[:] += df.apply(lambda x: re.findall(r"(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.,]* ([12][09]\d{2})",x))
    answer[:] += df.apply(lambda x: re.findall(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.,]*[ -](\d{1,2})[a-z,]{0,3}[ -]([12][09]\d{2})",x))
    answer[:] += df.apply(lambda x: re.findall(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.,]* ([12][09]\d{2})",x))
    answer[:] += df.apply(lambda x: re.findall(r"([12][09]\d{2})",x))
    answer = answer.apply(lambda x: x[0])

    def process(x):
        y = 1900
        m = 1
        d = 1

        month_dict = {"Jan":1,
                      "Feb":2,
                      "Mar":3,
                      "Apr":4,
                      "May":5,
                      "Jun":6,
                      "Jul":7,
                      "Aug":8,
                      "Sep":9,
                      "Oct":10,
                      "Nov":11,
                      "Dec":12}

        if type(x)==str:
            y = int(x)

        elif len(x)==2:
            y = int(x[1])

            try:
                m = int(x[0])
            except:
                m = month_dict[x[0][:3]]

        else:
            y = int(x[2])

            try:
                m = int(x[0])
                d = int(x[1])
            except:
                try:
                    m = month_dict[x[0][:3]]
                    d = int(x[1])
                except:
                    m = month_dict[x[1][:3]]
                    d = int(x[0])

        if y < 100:
            y += 1900

        result = date(y, m, d)
        return result

    answer = answer.apply(lambda x: process(x))
    answer = answer.rank().apply(int) - 1    
    answer = pd.Series(data=answer.index.values, index=answer.values).sort_index()
    return answer
