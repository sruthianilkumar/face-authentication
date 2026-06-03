import { View, Text, TouchableOpacity } from "react-native";
import { CameraView, useCameraPermissions } from "expo-camera";
import { useRef, useState } from "react";

export default function HomeScreen() {
  const cameraRef = useRef(null);
  const [permission, requestPermission] = useCameraPermissions();
  const [result, setResult] = useState("");

  if (!permission) return <View />;
  
  if (!permission.granted) {
    return (
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <Text>Camera permission required</Text>
        <TouchableOpacity onPress={requestPermission}>
          <Text style={{ marginTop: 10, color: "blue" }}>
            Grant Permission
          </Text>
        </TouchableOpacity>
      </View>
    );
  }

  const takePicture = async () => {
    const photo = await cameraRef.current?.takePictureAsync();
    setResult("Captured ✔ (next: send to backend)");
    console.log(photo);
  };

  return (
    <View style={{ flex: 1 }}>
      <CameraView ref={cameraRef} style={{ flex: 1 }} />

      <TouchableOpacity
        onPress={takePicture}
        style={{
          position: "absolute",
          bottom: 40,
          alignSelf: "center",
          backgroundColor: "white",
          padding: 15,
          borderRadius: 10,
        }}
      >
        <Text>Capture Face</Text>
      </TouchableOpacity>

      <Text style={{ position: "absolute", top: 50, alignSelf: "center" }}>
        {result}
      </Text>
    </View>
  );
}
