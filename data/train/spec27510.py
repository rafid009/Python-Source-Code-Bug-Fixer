import numpy as np 

def function(x):

	l3 = x
	p9 = 6
	paths = []
	try:
		if p9 >= 9:
			l3 = 3*l3
			paths.append(1)
		else:
			l3 = 5+9
			x = p9/l3
			p9 = 7-p9
			paths.append(2)
		if l3 > 7:
			p9 = x-p9
			paths.append(3)
		else:
			p9 = 6/8
			x = 1-9
			l3 = l3/9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))