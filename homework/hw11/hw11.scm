(define (find s predicate)
  (cond ((null? s) #f)
              ((predicate (car s)) (car s))
              (else (find (cdr-stream s) predicate))
  )
)

(define (scale-stream s k)
  (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k))
)

(define (has-cycle s)
    (define (helper haste lazy)
        (cond 
            ((or (null? haste) (null? (cdr-stream haste))) #f)
            ((eq? haste lazy) #t)
            (else (helper (cdr-stream (cdr-stream haste)) (cdr-stream lazy)))))
    (helper (cdr-stream s) s))
