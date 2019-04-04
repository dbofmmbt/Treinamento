struct noAB{
    int info;
    struct noAB * esq;
    struct noAB * dir;
};

AB * retira_abb(AB * a, int el){
    if (!a) return a;
    if (x > a->info)
        a->dir = retira_abb(a->dir, el);
    else if
        a->esq = retira_abb(a->esq, el);
    else{  // Achei X
        if ((!a->esq) && (!a->dir)){
            free(a);
            return NULL;
        } else if ((!a->esq) || (!a->dir)){
            AB * f;
            if (!a->dir) f = a->esq;
            else f = a->dir;
            free(a);
            return f;
        } else {
            AB * f = a->esq;
            while(f->dir) f = f->dir;
            a->info = f->info;
            f->info = x;
            a->esq = retira_abb(a->esq, x);
        }
    }
    return a;
}