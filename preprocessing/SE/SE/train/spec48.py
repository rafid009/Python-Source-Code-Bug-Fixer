import numpy as np 

def function(x):

	f6 = 2
	l3 = 4
	paths = []
	try:
		if f6 >= 7:
			l3 = 9*l3
			x = 1-8
			paths.append(1)
		else:
			l3 = f6+x
			f6 = 7*1
			l3 = 5-l3
			paths.append(2)
		if f6 > 0:
			x = x*2
			paths.append(3)
		else:
			f6 = 7-8
			f6 = f6+f6
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