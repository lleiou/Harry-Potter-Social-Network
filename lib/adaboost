#adaBoost returns the classifier
def adaBoost(X,y,B): #program does nothing as written
    def train(X, w, y):
        n = np.shape(X)[0]
        p = np.shape(X)[1]
        mode = np.repeat(0.0, p)
        theta = np.repeat(0.0, p)
        loss = np.repeat(0.0, p)

        # find optimal theta for every dimension j
        for j in range(p):
            # get the index of the order
            indx = sorted(range(len(X.iloc[:, j])), key=lambda k: X.iloc[:, j][k])
            x_j = X.iloc[indx, j]
            # using a cumulative sum, count the weight when progressively shifting the threshold to the right
            w_cum = np.cumsum(np.multiply(w[indx], y[indx]))
            # handle multiple occurrences of same x_j value: threshold
            # point must not lie between elements of same value
            ######################
            # w_cum[duplicates(List, x_j) == 1] = NA
            # find the optimum threshold and classify accordingl
            # m < - max(abs(w_cum), na.rm = TRUE)
            #########################
            m = max(abs(w_cum))
            # guarantee that the type of input is array:
            maxIndx = min([i for i in range(len(w_cum)) if abs(w_cum[i]) == m])
            mode[j] = (w_cum[maxIndx] < 0) * 2 - 1
            theta[j] = x_j[maxIndx]
            c = ((X.iloc[:, j] > theta[j]) * 2 - 1) * mode[j]
            loss[j] = np.dot(np.array(np.array(c.values) != y, dtype=float), w)
            # determine optimum dimension, threshold and comparison
            # for test only:
            #print c
        m = min(loss)
        j_star = min([i for i in range(len(loss)) if loss[i] == m])
        # pars < - dict(j=j_star, theta=theta[j_star], mode=mode[j_star])
        pars = [j_star, theta[j_star], mode[j_star]]
        return pars

    def classify(X, pars):
        label = (2 * (X.iloc[:, pars[0]] > pars[1]) - 1) * pars[2]
        return label

    n = np.shape(X)[0]
    w = np.ones(n)/n
    alpha = np.repeat(0.0,B)
    #allPars < - rep(list(list()), B)
    allPars = pd.DataFrame(index=range(B), columns=range(3))
    # boost base classifiers
    for b in range(B):
        # step a) train base classifier„
        allPars.iloc[b,:] = train(X, w, y)
        # step b) compute error
        missClass = np.array(np.array(classify(X, allPars.iloc[b, :])) != y, dtype=float)
        e = np.dot(w, missClass)/sum(w)
        # step c) compute voting weight
        if e==0:
            alpha[b] = 10
        else:
        #   alpha[b] = np.log((1 - e)/e)
            alpha[b] = np.log((1 - e)/e)
        # step d) recompute weights
        w = np.multiply(w, np.exp(np.multiply(alpha[b], missClass)))

    return [allPars, alpha]

#agg_class implement the classifier to a new dataset X, and returns the labels that it predicts.
def agg_class(X,alpha,allPars):
    n = np.shape(X)[0]
    B = len(alpha)
    Labels = pd.DataFrame(index=range(n), columns=range(B))

    for b in range(B):
        Labels.iloc[:, b] = classify(X, allPars.iloc[b, :])
        # weight classifier response with respective alpha coefficient
    Labels = np.dot(Labels, alpha)
    c_hat = np.sign(Labels)
    return(c_hat)
