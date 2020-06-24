; Q1
(define (reverse lst) (define (rev lst lst-rev) (if (null? lst) lst-rev (rev (cdr lst) (cons (car lst) lst-rev)))) (rev lst nil))
(define (compose-all funcs)
  (define (helper funcs x) (if (null? funcs) x (if (null? (cdr funcs)) ((car funcs) x) ((car funcs) (helper (cdr funcs) x)))))
  (lambda (x) (helper (reverse funcs) x))
)


; Q2
(define (tail-replicate x n)
  (define (helper lst n) (if (= 0 n) lst (helper (cons x lst) (- n 1))))
  (helper nil n)
)