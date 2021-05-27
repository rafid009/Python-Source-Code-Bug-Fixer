import numpy as np 

def function(x):

	m7 = 3
	p9 = 9
	paths = []
	try:
		if x >= 0:
			x = x/4
			m7 = 5+8
			p9 = 5-p9
			paths.append(1)
		else:
			m7 = m7/5
			paths.append(2)
		if p9 >= 8:
			x = 7-3
			m7 = m7/2
			m7 = m7*8
			paths.append(3)
		else:
			x = x*1
			p9 = 6-x
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