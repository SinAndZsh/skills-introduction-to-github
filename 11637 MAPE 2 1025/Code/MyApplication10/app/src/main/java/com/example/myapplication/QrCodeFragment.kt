package com.example.myapplication

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import androidx.fragment.app.Fragment

class QrCodeFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_qr_code, container, false)
        val qrCodeImageView = view.findViewById<ImageView>(R.id.qr_code_image)
        // 使用新添加的二维码图片
        qrCodeImageView.setImageResource(R.drawable.custom_qr_code)
        return view
    }
}