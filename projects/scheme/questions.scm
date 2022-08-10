(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
    (define enum-with-index 
      (lambda (str start) 
        (if (null? str)
          start
          (enum-with-index ;Tail Calls
            (cdr str) 
            (append start (list (list (length start) (car str))))
          )
        )
      )
    )
    (enum-with-index s nil)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  ; BEGIN PROBLEM 16
  (define (merge-inner inorderi? list1i list2i start)
    (let ((is-nil1 (null? list1i)) 
      (is-nil2 (null? list2i)))
      ; (print list1i)(print list2i)(print is-nil1)(print is-nil2)
    (cond ((and is-nil1 is-nil2) start) ; both list is nil 
      ((and is-nil1 (not is-nil2)) (append start list2i)) ; list1 is nil
      ((and is-nil2 (not is-nil1)) (append start list1i)) ; list2 is nil
      (else ( ; neither is nil
        cond ((inorderi? (car list1i) (car list2i))  (merge-inner inorderi? 
            (cdr list1i) 
            list2i 
            (append start (list (car list1i)))))
          (else  (merge-inner inorderi? 
            list1i 
            (cdr list2i) 
            (append start (list (car list2i)))))
      )) 
    ))
  )
  (merge-inner inorder? list1 list2 nil)
)
  ; END PROBLEM 16


;; Optional Problem 1

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         expr ; expr = (quote rest)
         ; END PROBLEM 17
         )
        ((or (lambda? expr) ; (lambda (a b)(+ a b))
             (define? expr)) ; (define a 1)  (define (f x y) (+ x y))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM 17
           ))
        ((let? expr) ;(let ((a 1) (b 2)) (+ a b))
         (let ((values (cadr expr)) ;(a 1) (b 2)
               (body   (cddr expr))) ;((+ a b ))
                ; ((a b) (1 2))
                
           ; BEGIN PROBLEM 17
           (let ((params (map (lambda (x) (car x)) values))
                 (actual-values (map (lambda (x) (let-to-lambda (cadr x))) values)))
            (cons (cons 'lambda (cons params (map let-to-lambda body))) actual-values)
           )
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
          (map let-to-lambda expr)
         ; END PROBLEM 17
         )))



;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'replace-this-line
  )
  ; END Question 21