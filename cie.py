import numpy as np
import matplotlib.pyplot as plt
import colour
from reflect import blackbody_radiation_intensity, sum_temp

# 输入可见光光谱的函数 (波长范围从380nm到780nm)
def input_spectrum():
    wavelength = np.arange(380, 781, 1).astype(float)
    intensity = blackbody_radiation_intensity(sum_temp, wavelength)  
    # intensity = np.ones_like(wavelength)  # 均匀光强
    intensity = intensity / wavelength ** 4
    return wavelength, intensity

# 计算三刺激值
def calculate_tristimulus_values(wavelengths, intensities):
    # 创建光谱分布对象
    sd = colour.SpectralDistribution(dict(zip(wavelengths, intensities)))

    # 使用CIE 1931色匹配函数计算三刺激值
    XYZ = colour.sd_to_XYZ(sd)
    return XYZ

# 将XYZ值转换为RGB
def xyz_to_rgb(XYZ):
    # 将XYZ转换为sRGB颜色空间
    XYZ = XYZ/XYZ.max()
    rgb = colour.XYZ_to_sRGB(XYZ)

    # 裁剪到[0, 1]范围
    rgb = np.clip(rgb, 0, 1)
    return rgb

# 可视化计算出的颜色
def visualize_color(rgb):
    # 创建一个1x1的图像，显示相应的颜色
    plt.figure(figsize=(2, 2))
    plt.imshow([[rgb]])
    plt.axis('off')
    plt.show()

# 主程序
def main():
    # Step 1: 输入光谱数据
    wavelengths, intensities = input_spectrum()
    
    # Step 2: 计算三刺激值
    XYZ = calculate_tristimulus_values(wavelengths, intensities)
    
    # Step 3: 将XYZ转换为RGB颜色
    rgb = xyz_to_rgb(XYZ)
    print((rgb*255).astype(int))
    
    # Step 4: 可视化颜色
    visualize_color(rgb)

if __name__ == "__main__":
    main()
