import numpy as np 

def function(x):

	w6 = x
	l3 = 9
	paths = []
	try:
		if x < 4:
			x = 3+l3
			paths.append(1)
		else:
			l3 = w6-l3
			paths.append(2)
		if l3 >= 2:
			w6 = w6*1
			l3 = x*0
			paths.append(3)
		else:
			x = 6-x
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