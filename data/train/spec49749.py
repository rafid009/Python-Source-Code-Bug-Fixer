import numpy as np 

def function(x):

	m1 = x
	p9 = 2
	paths = []
	try:
		if x > 1:
			m1 = x-2
			m1 = x/3
			paths.append(1)
		else:
			p9 = 7+p9
			p9 = m1*7
			paths.append(2)
		if p9 > 3:
			p9 = p9*0
			paths.append(3)
		else:
			m1 = p9*m1
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		m1 = p9**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))