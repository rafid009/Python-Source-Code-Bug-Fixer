import numpy as np 

def function(x):

	m7 = x
	p9 = x
	paths = []
	try:
		if p9 <= 9:
			x = 1/x
			p9 = p9-p9
			paths.append(1)
		else:
			x = 7-x
			p9 = p9+9
			m7 = 5+7
			paths.append(2)
		if x < 7:
			x = x*7
			p9 = p9/9
			paths.append(3)
		else:
			p9 = 4+3
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		p9 = m7**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))