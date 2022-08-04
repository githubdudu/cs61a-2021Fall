scm> (define a 1)
;a

scm> a
;1

scm> (define b a)
;b

scm> b
;1

scm> (define c 'a)
;c

scm> c
;a




scm> (define a (+ 1 2))
;a
scm> a
;3
scm> (define b (- (+ (* 3 3) 2) 1))
;b
scm> (+ a b)
;13
scm> (= (modulo b a) (quotient 5 3))
;#t


scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1
scm> ((if (< 4 3) + -) 4 100)
-96