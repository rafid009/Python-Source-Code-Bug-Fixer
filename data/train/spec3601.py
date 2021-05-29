import numpy as np 

def function(x):

	f2 = x
	m5 = x
	paths = []
	try:
		if f2 < 9:
			x = 7/x
			x = x+m5
			f2 = 8+6
			paths.append(1)
		else:
			x = x+1
			x = 4*x
			paths.append(2)
		if f2 <= 2:
			m5 = m5*9
			x = x*5
			m5 = m5/m5
			paths.append(3)
		else:
			x = x-6
			f2 = f2*f2
			m5 = m5*1
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