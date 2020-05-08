def old_predict_views():
    with open('predict.txt','r') as f:
        variable = f.read()
        return (int(variable))
def count_views():
    with open('views.txt','r+') as f:
        variable = f.read()
        variable=int(variable)
        variable+=1
        f.seek(0)
        f.truncate(0)
        f.write(str(variable))
        return (int(variable))
def predict_views():
    with open('predict.txt','r+') as f:
        variable = f.read()

        variable=int(variable)
        variable+=1
        f.seek(0)
        f.truncate(0)
        f.write(str(variable))
        return (int(variable))