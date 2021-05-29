import numpy as np 

def function(x):

	p3 = 5
	m5 = 0
	paths = []
	try:
		if m5 <= 8:
			p3 = p3+2
			p3 = p3+x
			m5 = 2+x
			paths.append(1)
		else:
			m5 = m5-6
			x = 6+x
			m5 = 3-p3
			paths.append(2)
		if m5 >= 3:
			x = x*5
			paths.append(3)
		else:
			p3 = 4+6
			x = p3+x
			x = x*0
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))