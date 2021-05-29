import numpy as np 

def function(x):

	w6 = 7
	p6 = x
	x = 0
	paths = []
	try:
		if p6 <= 6:
			p6 = p6+w6
			x = 5+2
			paths.append(1)
		else:
			p6 = p6*4
			p6 = p6+1
			paths.append(2)
		if x < 4:
			p6 = p6+6
			p6 = p6*9
			paths.append(3)
		else:
			w6 = x+w6
			p6 = p6*7
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))