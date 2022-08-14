; Define a function nondecreaselist, which takes in a scheme list of numbers and outputs a list of lists, which overall has the same numbers in the same order, but grouped into lists that are non-decreasing.

; scm> (1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1)
; ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1))
(define (nondecreaselist s)

(1 2 3 1 2 3), 1, (2 3 1 2 3)

    (if (null? s)
        s
        (let ((rest (nondecreaselist (cdr s))))
            (if (or (null? rest) (> (car s)(car (car rest))))
                (cons (cons (car s) nil) rest)
                (cons (cons (car s) (car rest)) (cdr rest))
            )
        )
    )
)

(expect (nondecreaselist '(1 2 3 1 2 3)) ((1 2 3) (1 2 3)))

(expect (nondecreaselist '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
        ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1)))
