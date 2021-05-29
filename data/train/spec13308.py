import numpy as np 

def function(x):

	p6 = 7
	t7 = 5
	x = 7
	paths = []
	try:
		if p6 <= 2:
			x = x+5
			paths.append(1)
		else:
			t7 = 5*2
			paths.append(2)
		if p6 <= 5:
			t7 = x+t7
			x = 9*t7
			paths.append(3)
		else:
			p6 = p6*0
			x = x-4
			t7 = x-t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		p6 = t7**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))