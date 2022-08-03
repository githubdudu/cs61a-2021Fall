(define (my-filter func lst) 
  (if (null? lst)
      '()  
      (if (func (car lst))
          (cons (car lst) (my-filter func (cdr lst)))
          (my-filter func (cdr lst)) 
      )  
  )
)

(define (interleave s1 s2) 
  (cond ((and (null? s1) (null? s2)) '())
      ((null? s1) s2)
      ((null? s2) s1)
      (else (cons (car s1) (cons (car s2) (interleave (cdr s1) (cdr s2)))))
  )
)

(define (accumulate merger start n term)
  (if (= n 1)
      (merger start (term n))
      (merger (accumulate merger start (- n 1) term) (term n))
  )
)

(define (no-repeats lst) 
  ; Judge first element
( begin
  (define (nore-add head rest-lst) 
    (if (null? rest-lst)
        head ; there is no more, return head
        (if (null? (my-filter (lambda (ele)(= ele (car rest-lst))) head))  ; first not in before
            (nore-add (append head (list (car rest-lst))) (cdr rest-lst)) ; recursion, update head and rest-lst
            (nore-add head (cdr rest-lst))
        )
    )
  )
  (nore-add '() lst)
)
)