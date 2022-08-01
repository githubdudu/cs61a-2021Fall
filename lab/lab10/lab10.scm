;(define (over-or-under num1 num2) (if 
;    (< num1 num2) 
;    -1 
;    (if 
;        (= num1 num2) 
;        0 
;        1
;    )
;    )
;)

(define (over-or-under num1 num2) 
    (cond 
        ((< num1 num2) -1)
        ((= num1 num2) 0)
        (else 1)
    )
)
(define (make-adder num) 
    (lambda (x) (+ x num))
)

(define (composed f g) 
    (lambda (x) (f (g x)))
)

; (define lst 
;     (cons (cons 1 nil)(cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))
; )
; (define lst 
;     (list (list 1) 2 (list 3 4) 5)
; )
(define lst 
    '((1) 2 (3 4) 5)
)

(define (remove item lst)
    (if (null? lst)
        lst
        (filter (lambda (x) (not (= x item))) lst)
    )
)
