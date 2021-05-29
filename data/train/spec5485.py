import numpy as np 

def function(x):

	t2 = x
	l3 = 5
	paths = []
	try:
		if l3 > 8:
			t2 = t2-t2
			x = x*l3
			paths.append(1)
		else:
			t2 = x*t2
			paths.append(2)
		if x >= 0:
			t2 = 2+x
			l3 = l3-7
			x = t2-2
			paths.append(3)
		else:
			t2 = t2/2
			x = 7/x
			t2 = 0*t2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))