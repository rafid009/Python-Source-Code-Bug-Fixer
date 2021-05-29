import numpy as np 

def function(x):

	m9 = 8
	p9 = x
	paths = []
	try:
		if p9 >= 5:
			p9 = p9/9
			p9 = p9-6
			paths.append(1)
		else:
			x = 3+6
			x = p9-p9
			m9 = 4+m9
			paths.append(2)
		if p9 < 6:
			x = 8+8
			m9 = m9-x
			m9 = p9/3
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		p9 = m9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))