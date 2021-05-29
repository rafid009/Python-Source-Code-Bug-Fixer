import numpy as np 

def function(x):

	p3 = 9
	r4 = x
	x = 0
	paths = []
	try:
		if p3 > 0:
			r4 = 6*r4
			paths.append(1)
		else:
			x = p3*2
			paths.append(2)
		if r4 >= 4:
			r4 = x/1
			r4 = 0+0
			r4 = r4+7
			paths.append(3)
		else:
			p3 = 7-p3
			p3 = p3*8
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))