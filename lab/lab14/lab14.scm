; scm> (car (split-at '(2 4 6 8 10) 3))
; (2 4 6)
; scm> (cdr (split-at '(2 4 6 8 10) 3))
; (8 10)
(define (split-at lst n) 
    (define (split-at-initial init lst n)
        (if (or (zero? n) (null? lst))
            (cons init lst)
            (split-at-initial (append init (list (car lst))) (cdr lst) (- n 1)))
    )
    (split-at-initial () lst n)
)

; scm> (define (square x) (* x x))
; square
; scm> (define (add-one x) (+ x 1))
; add-one
; scm> (define (double x) (* x 2))
; double
; scm> (define composed (compose-all (list double square add-one)))
; composed
; scm> (composed 1)
; 5
; scm> (composed 2)
; 17
(define (compose-all funcs)
    (define (outer n) 
        (define (compose-all-inner init funcs) 
            (if (null? funcs)
                init
                (compose-all-inner ((car funcs) init) (cdr funcs))))
        (compose-all-inner n funcs)
    )
    outer ; expose outer func to outside, cause define will just return a str "outer"
)
