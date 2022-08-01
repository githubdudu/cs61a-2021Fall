(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s))
)

(define (caddr s) 
    (car (cddr s))
)

(define (ordered? s) 
    (if (null? s)
        #t
        (if(null? (cdr s))
            #t
            (and (<= (car s) (cadr s))
                (ordered? (cdr s))
            )
        )
    )
)

(define (square x) (* x x))

(define (pow base exp) 
    (if (= exp 2)
        (square base)
        (if (even? exp)
            (square (pow base (/ exp 2)))
            (* base (pow base (- exp 1)))
        )
    )
)
