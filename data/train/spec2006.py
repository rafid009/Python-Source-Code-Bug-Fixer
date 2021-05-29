import numpy as np 

def function(x):

	h2 = x
	l1 = x
	paths = []
	try:
		if x > 8:
			x = 2+x
			l1 = x/9
			h2 = h2-2
			paths.append(1)
		else:
			x = 9-9
			l1 = h2+9
			x = h2+0
			paths.append(2)
		if l1 <= 9:
			x = x*1
			x = x/9
			x = x/2
			paths.append(3)
		else:
			l1 = h2*h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		l1 = h2**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))