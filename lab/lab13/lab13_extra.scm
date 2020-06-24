; Q4
(define (rle s)
  (define (helper s n)
    (cond ((null? (cdr-stream s)) (cons-stream (list (car s) n) nil)) 
      ((= (car s) (car (cdr-stream s))) (helper (cdr-stream s) (+ 1 n))) 
      (else (cons-stream (list (car s) n) (rle (cdr-stream s)))))
  )
  (if (null? s) nil (helper s 1))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  (define (helper n before after)
    (if (< n (car after)) 
        (append before (append (cons n nil) after))
        (if (null? (cdr after)) 
            (append s (cons n nil))
            (helper n (append before (cons (car after) nil)) (cdr after)))
    )
  )
  (helper n nil s)
)

; Q6
(define (deep-map fn s)
    (cond 	((null? s) nil)
            	((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
	(else (cons (fn (car s)) (deep-map fn (cdr s))))
    )
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  (if (null? s) nil (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))
)

(define (count name s)
    (cond	((null? s) 0)
	((eq? (car s) name) (+ 1 (count name (cdr s))))
	(else (count name (cdr s)))
    )
)

(define (tally names)
  (map (lambda (x) (cons x (count x names))) (unique names))
)