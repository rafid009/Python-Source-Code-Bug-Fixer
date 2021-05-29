import numpy as np 

def function(x):

	l1 = x
	r3 = x
	paths = []
	try:
		if l1 > 7:
			l1 = l1*8
			l1 = l1/1
			r3 = 1/r3
			paths.append(1)
		else:
			x = x/9
			l1 = l1-5
			paths.append(2)
		if r3 > 2:
			l1 = x/5
			paths.append(3)
		else:
			l1 = l1+l1
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))